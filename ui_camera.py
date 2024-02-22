# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.setEnabled(True)
        Camera.resize(921, 580)
        self.actionExit = QAction(Camera)
        self.actionExit.setObjectName(u"actionExit")
        self.actionStartCamera = QAction(Camera)
        self.actionStartCamera.setObjectName(u"actionStartCamera")
        self.actionStopCamera = QAction(Camera)
        self.actionStopCamera.setObjectName(u"actionStopCamera")
        self.actionSet = QAction(Camera)
        self.actionSet.setObjectName(u"actionSet")
        self.actionAbout = QAction(Camera)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actiondevice = QAction(Camera)
        self.actiondevice.setObjectName(u"actiondevice")
        self.centralwidget = QWidget(Camera)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(145, 145, 145, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.stackedWidget.setPalette(palette)
        self.viewfinderPage = QWidget()
        self.viewfinderPage.setObjectName(u"viewfinderPage")
        self.gridLayout_5 = QGridLayout(self.viewfinderPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.viewfinder = QVideoWidget(self.viewfinderPage)
        self.viewfinder.setObjectName(u"viewfinder")

        self.gridLayout_5.addWidget(self.viewfinder, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.viewfinderPage)
        self.previewPage = QWidget()
        self.previewPage.setObjectName(u"previewPage")
        self.gridLayout_4 = QGridLayout(self.previewPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lastImagePreviewLabel = QLabel(self.previewPage)
        self.lastImagePreviewLabel.setObjectName(u"lastImagePreviewLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lastImagePreviewLabel.sizePolicy().hasHeightForWidth())
        self.lastImagePreviewLabel.setSizePolicy(sizePolicy1)
        self.lastImagePreviewLabel.setFrameShape(QFrame.Box)

        self.gridLayout_4.addWidget(self.lastImagePreviewLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.previewPage)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 2, 1)

        self.captureWidget = QTabWidget(self.centralwidget)
        self.captureWidget.setObjectName(u"captureWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setEnabled(True)
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.takeImageButton = QPushButton(self.tab_2)
        self.takeImageButton.setObjectName(u"takeImageButton")
        self.takeImageButton.setEnabled(True)

        self.gridLayout.addWidget(self.takeImageButton, 0, 0, 1, 1)

        self.autoAF = QPushButton(self.tab_2)
        self.autoAF.setObjectName(u"autoAF")
        self.autoAF.setEnabled(True)
        self.autoAF.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.autoAF, 1, 0, 1, 1)

        self.autoExpo = QPushButton(self.tab_2)
        self.autoExpo.setObjectName(u"autoExpo")
        self.autoExpo.setEnabled(True)
        self.autoExpo.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.autoExpo, 2, 0, 1, 1)

        self.autoWB = QPushButton(self.tab_2)
        self.autoWB.setObjectName(u"autoWB")
        self.autoWB.setEnabled(True)
        self.autoWB.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.autoWB, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.scanButton = QPushButton(self.tab_2)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setEnabled(True)
        self.scanButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.scanButton, 5, 0, 1, 1)

        self.stitchButton = QPushButton(self.tab_2)
        self.stitchButton.setObjectName(u"stitchButton")
        self.stitchButton.setEnabled(True)
        self.stitchButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.stitchButton, 6, 0, 1, 1)

        self.captureWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stopButton = QPushButton(self.tab)
        self.stopButton.setObjectName(u"stopButton")

        self.gridLayout_2.addWidget(self.stopButton, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.recordButton = QPushButton(self.tab)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setCursor(QCursor(Qt.ArrowCursor))
        self.recordButton.setToolTipDuration(-5)

        self.gridLayout_2.addWidget(self.recordButton, 0, 0, 1, 1)

        self.pauseButton = QPushButton(self.tab)
        self.pauseButton.setObjectName(u"pauseButton")

        self.gridLayout_2.addWidget(self.pauseButton, 1, 0, 1, 1)

        self.captureWidget.addTab(self.tab, "")

        self.gridLayout_3.addWidget(self.captureWidget, 1, 1, 1, 2)

        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Camera)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 921, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDevices = QMenu(self.menubar)
        self.menuDevices.setObjectName(u"menuDevices")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        Camera.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Camera)
        self.statusbar.setObjectName(u"statusbar")
        Camera.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevices.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionStartCamera)
        self.menuFile.addAction(self.actionStopCamera)
        self.menuFile.addSeparator()
        self.menuDevices.addAction(self.actiondevice)
        self.menuHelp.addAction(self.actionAbout)
        self.menu.addAction(self.actionSet)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)

        self.retranslateUi(Camera)
        self.actionSet.triggered.connect(Camera.configureCaptureSettings)
        self.scanButton.clicked.connect(Camera.scanSettings)

        self.stackedWidget.setCurrentIndex(1)
        self.captureWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Camera", None))
        self.actionExit.setText(QCoreApplication.translate("Camera", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Camera", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionStartCamera.setText(QCoreApplication.translate("Camera", u"\u542f\u52a8\u76f8\u673a", None))
        self.actionStopCamera.setText(QCoreApplication.translate("Camera", u"\u505c\u6b62\u76f8\u673a", None))
        self.actionSet.setText(QCoreApplication.translate("Camera", u"\u6587\u4ef6\u8bbe\u7f6e", None))
        self.actionAbout.setText(QCoreApplication.translate("Camera", u"About us", None))
        self.actiondevice.setText(QCoreApplication.translate("Camera", u"\u68c0\u6d4b\u626b\u63cf\u8bbe\u5907", None))
        self.lastImagePreviewLabel.setText("")
        self.takeImageButton.setText(QCoreApplication.translate("Camera", u"\u6355\u83b7\u56fe\u50cf", None))
        self.autoAF.setText(QCoreApplication.translate("Camera", u"\u624b\u52a8\u5bf9\u7126", None))
        self.autoExpo.setText(QCoreApplication.translate("Camera", u"\u81ea\u52a8\u66dd\u5149", None))
        self.autoWB.setText(QCoreApplication.translate("Camera", u"\u81ea\u52a8\u767d\u5e73\u8861", None))
        self.scanButton.setText(QCoreApplication.translate("Camera", u"\u542f\u52a8\u626b\u63cf", None))
        self.stitchButton.setText(QCoreApplication.translate("Camera", u"\u6267\u884c\u62fc\u63a5", None))
        self.captureWidget.setTabText(self.captureWidget.indexOf(self.tab_2), QCoreApplication.translate("Camera", u"\u626b\u63cf", None))
        self.stopButton.setText(QCoreApplication.translate("Camera", u"\u7ed3\u675f", None))
        self.recordButton.setText(QCoreApplication.translate("Camera", u"\u5f00\u59cb\u5f55\u50cf", None))
        self.pauseButton.setText(QCoreApplication.translate("Camera", u"\u6682\u505c", None))
        self.captureWidget.setTabText(self.captureWidget.indexOf(self.tab), QCoreApplication.translate("Camera", u"\u5f55\u50cf", None))
        self.menuFile.setTitle(QCoreApplication.translate("Camera", u"\u76f8\u673a", None))
        self.menuDevices.setTitle(QCoreApplication.translate("Camera", u"\u626b\u63cf\u8bbe\u5907", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Camera", u"\u5e2e\u52a9", None))
        self.menu.setTitle(QCoreApplication.translate("Camera", u"\u8bbe\u7f6e", None))
    # retranslateUi

