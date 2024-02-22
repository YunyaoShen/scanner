# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ScanUi(object):
    def setupUi(self, ScanUi):
        if not ScanUi.objectName():
            ScanUi.setObjectName(u"ScanUi")
        ScanUi.resize(377, 315)
        self.gridLayout = QGridLayout(ScanUi)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 14, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ScanUi)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(ScanUi)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.imageCodecBox = QComboBox(self.groupBox_2)
        self.imageCodecBox.setObjectName(u"imageCodecBox")

        self.gridLayout_2.addWidget(self.imageCodecBox, 5, 0, 1, 2)

        self.imageResolutionBox = QComboBox(self.groupBox_2)
        self.imageResolutionBox.setObjectName(u"imageResolutionBox")

        self.gridLayout_2.addWidget(self.imageResolutionBox, 1, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.retranslateUi(ScanUi)
        self.buttonBox.accepted.connect(ScanUi.accept)
        self.buttonBox.rejected.connect(ScanUi.reject)

        QMetaObject.connectSlotsByName(ScanUi)
    # setupUi

    def retranslateUi(self, ScanUi):
        ScanUi.setWindowTitle(QCoreApplication.translate("ScanUi", u"Image Settings", None))
        self.groupBox_2.setTitle("")
        self.label_8.setText(QCoreApplication.translate("ScanUi", u"\u7269\u955c\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("ScanUi", u"\u5b58\u50a8\u8def\u5f84", None))
    # retranslateUi

