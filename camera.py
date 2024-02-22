# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import os
from pathlib import Path

from PySide6.QtMultimedia import (QAudioInput, QCamera, QCameraDevice,
                                  QImageCapture, QMediaCaptureSession,
                                  QMediaDevices, QMediaMetaData,
                                  QMediaRecorder)
from PySide6.QtWidgets import QDialog, QMainWindow, QMessageBox
from PySide6.QtGui import QAction, QActionGroup, QIcon, QImage, QPixmap
from PySide6.QtCore import QDateTime, QDir, QTimer, Qt, Slot, qWarning


from imagesettings import ImageSettings
from scan import Scan
from ui_camera import Ui_Camera

# import sys, uvcham
from PySide6.QtCore import Signal, QTimer
import Com
import time
from PySide6.QtCore import QThread


llll
class MyThread(QThread):
    sinSnap = Signal()
    sinAF = Signal()
    sinAutoAF = Signal()

    def __init__(self):
        super().__init__()
        self.state = 0

    def accept(self,num):    #接受Ui线程也就是主线程传参
        self.state = num
        print(self.state)

    def run(self):
        moveCommand = bytearray([0x55, 0x01, 0x01, 0x04, 0x13, 0x00, 0x01, 0x90])
        directionCommand = bytearray([0x55, 0x01, 0x01, 0x04, 0x15, 0x00, 0x00, 0x8F])
        setRowCommand = bytearray([0x55, 0x01, 0x01, 0x04, 0x16, 0x00, 0x01, 0x8D])
        setColumnCommand = bytearray([0x55, 0x01, 0x01, 0x04, 0x17, 0x00, 0x02, 0x8B])
        wrapColumnCommand = bytearray([0x55, 0x01, 0x01, 0x04, 0x18, 0x00, 0x00, 0x8C])
        originCommand = bytearray([0x55, 0x01, 0x01, 0x04, 0x19, 0x00, 0x00, 0x8B])

        com = Com.COM("COM3", 9600)
        com.open()
        # 初始设置
        com.send_data(originCommand)
        time.sleep(4)
        print(com.send_data(directionCommand))
        print(com.send_data(setRowCommand))
        print(com.send_data(setColumnCommand))
        time.sleep(2)


        # 偏置移动量
        for i in range(0):
            print(com.send_data(wrapColumnCommand))
            time.sleep(2)

        # 设置载玻片长度长为2*5cm,设置行间距为50微米，列间距为100微米
        row = int(600 / 50) + 1
        column = int(2800 / 100) + 1
        for i in range(0, row):
            for j in range(0, column):
                # self.sinAF.emit()
                self.sinSnap.emit()
                time.sleep(2)
                print(com.send_data(moveCommand))
                self.state = 0
                time.sleep(2)
            print(com.send_data(wrapColumnCommand))
            time.sleep(3)
        com.close()

class Camera(QMainWindow):
    evtCallback = Signal(int)
    mainsignal = Signal(int)
    def __init__(self):
        super().__init__()
        self.hcam = None
        self.imgWidth = 0
        self.imgHeight = 0
        self.pData = None
        self.frame = 0
        self.count = 0
        self.timer = QTimer(self)
        self._ui = Ui_Camera()
        self._ui.setupUi(self)
        self.evtCallback.connect(self.onevtCallback)


    def eventCallBack(nEvent, self):
        '''callbacks come from uvcham.dll internal threads, so we use qt signal to post this event to the UI thread'''
        self.evtCallback.emit(nEvent)

    def onevtCallback(self, nEvent):
        '''this run in the UI thread'''
        if self.hcam is not None:
            if uvcham.UVCHAM_EVENT_IMAGE & nEvent != 0:
                self.onImageEvent()
            elif uvcham.UVCHAM_EVENT_ERROR & nEvent != 0:
                self.closeCamera()
                QMessageBox.warning(self, "Warning", "Generic error.")
            elif uvcham.UVCHAM_EVENT_DISCONNECT & nEvent != 0:
                self.closeCamera()
                QMessageBox.warning(self, "Warning", "Camera disconnect.")

    def onBtnScan(self):
        self.thread_ = MyThread()
        self.thread_.sinSnap.connect(self.onBtnSnap)
        self.thread_.sinAF.connect(self.getAF)
        self.thread_.sinAutoAF.connect(self.onAutoAF)
        self.thread_.start()


    def  onAutoExpo(self, state):
        if self.hcam is not None:
            self.hcam.put(uvcham.UVCHAM_AEXPO, 1 )
            # self.slider_expoTime.setEnabled(not state)
            # self.slider_expoGain.setEnabled(not state)
    def onWB(self):
        if self.hcam is not None:
            self.hcam.put(uvcham.UVCHAM_WBMODE, 1)

    def onFZ(self):
        if self.hcam is not None:
            self.hcam.put(uvcham.UVCHAM_FLIPVERT, 1)
    def onAutoAF(self,pos = 2):
        if self.hcam is not None:
            print(123)
            self.hcam.put(uvcham.UVCHAM_AFMODE, 2)


    def getAF(self):
        if self.hcam is not None:
            self.onAutoAF(2)
            while True:
                self.AFstate = self.hcam.get(uvcham.UVCHAM_AFFEEDBACK)

                if(self.AFstate == 1):

                    break
                if (self.AFstate == 2):
                    continue
                self.onAutoAF(2)
            self.mainsignal.emit(self.AFstate)
            self.mainsignal.connect(self.thread_.accept)

    def openCamera(self, id):
        self.hcam = uvcham.Uvcham.open(id)
        if self.hcam:
            self.frame = 0
            self.hcam.put(uvcham.UVCHAM_FORMAT, 2) #Qimage use RGB byte order
            # self.hcam.put(uvcham.UVCHAM_FLIPHORZ, 1)
            res = self.hcam.get(uvcham.UVCHAM_RES)
            self.imgWidth = self.hcam.get(uvcham.UVCHAM_WIDTH | res)
            self.imgHeight = self.hcam.get(uvcham.UVCHAM_HEIGHT | res)
            self.pData = bytes(uvcham.TDIBWIDTHBYTES(self.imgWidth * 24) * self.imgHeight)
            try:
                self.hcam.start(None, self.eventCallBack, self) # Pull Mode
            except uvcham.HRESULTException:
                self.closeCamera()
                QMessageBox.warning(self, "Warning", "Failed to start camera.")
            else:
                # self.cbox_auto.setEnabled(True)
                # self.btn_autoWB.setEnabled(True)
                # self.btn_open.setText("Close")
                # self.btn_scan.setEnabled(True)
                # self.btn_autoAF.setEnabled(True)

                nmin, nmax, ndef = self.hcam.range(uvcham.UVCHAM_EXPOTIME)
                # self.slider_expoTime.setRange(nmin, nmax)
                nmin, nmax, ndef = self.hcam.range(uvcham.UVCHAM_AGAIN)
                # self.slider_expoGain.setRange(nmin, nmax)
                bAuto = self.hcam.get(uvcham.UVCHAM_AEXPO)
                # self.cbox_auto.setChecked(1 == bAuto)
                # self.slider_expoTime.setEnabled(1 != bAuto)
                # self.slider_expoGain.setEnabled(1 != bAuto)
                # self.updateExpoTime()
                # self.updateGain()

                # self.timer.start(1000)


    def onBtnOpen(self):
        if self.hcam is not None:
            self.closeCamera()
        else:
            arr = uvcham.Uvcham.enum()
            if len(arr) == 0:
                QMessageBox.warning(self, "Warning", "No camera found.")
            elif 1 == len(arr):
                self.openCamera(arr[0].id)
            else:
                print("这里重写多个设备的状况下的情况")
                # menu = QMenu()
                # for i in range(0, len(arr)):
                #     action = QAction(arr[i].displayname, self)
                #     action.setData(i)
                #     menu.addAction(action)
                # action = menu.exec(self.mapToGlobal(self.btn_open.pos()))
                # if action:
                #     self.openCamera(arr[action.data()].id)

    def onBtnSnap(self):
        if self.hcam is not None and self.pData is not None:
            image = QImage(self.pData, self.imgWidth, self.imgHeight, QImage.Format_RGB888)
            self.count += 1
            image.save("./file/pyqt{}.jpg".format(self.count))

    def onImageEvent(self):
        self.hcam.pull(self.pData) # Pull Mode
        self.frame += 1
        image = QImage(self.pData, self.imgWidth, self.imgHeight, QImage.Format_RGB888)
        newimage = image.scaled(self.lbl_video.width(), self.lbl_video.height(), Qt.KeepAspectRatio, Qt.FastTransformation)
        self.lbl_video.setPixmap(QPixmap.fromImage(newimage))

    def closeCamera(self):
        if self.hcam:
            self.hcam.close()
        self.hcam = None
        self.pData = None

        # self.btn_open.setText("Open")
        # self.timer.stop()
        # self.lbl_frame.clear()
        # self.cbox_auto.setEnabled(False)
        # self.slider_expoGain.setEnabled(False)
        # self.slider_expoTime.setEnabled(False)
        # self.btn_autoWB.setEnabled(False)
        # self.btn_scan.setEnabled(False)

    def closeEvent(self, event):
        if self.hcam is not None:
            self.hcam.close()
            self.hcam = None

    @Slot()
    def configureCaptureSettings(self):
        settings_dialog = ImageSettings()

        if settings_dialog.exec():
            settings_dialog.apply_image_settings()

    @ Slot()
    def scanSettings(self):
        settings_dialog = Scan()

        if settings_dialog.exec():
            print("开始扫描")
