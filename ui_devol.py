# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_devolv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WinDevol(object):
    def setupUi(self, WinDevol):
        if not WinDevol.objectName():
            WinDevol.setObjectName(u"WinDevol")
        WinDevol.resize(471, 273)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WinDevol.sizePolicy().hasHeightForWidth())
        WinDevol.setSizePolicy(sizePolicy)
        WinDevol.setMinimumSize(QSize(471, 273))
        WinDevol.setMaximumSize(QSize(471, 273))
        WinDevol.setStyleSheet(u"background-color:rgb(25, 25, 25)")
        self.frame = QFrame(WinDevol)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 452, 283))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color:rgb(25, 25, 25)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 1, 452, 270))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(112, 56, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(112, 56, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(450, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(8)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txt_cod_devol = QLineEdit(self.layoutWidget)
        self.txt_cod_devol.setObjectName(u"txt_cod_devol")
        self.txt_cod_devol.setStyleSheet(u"color:rgb(255,255,255)")

        self.horizontalLayout_2.addWidget(self.txt_cod_devol)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(450, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.btn_voltar_devolv = QPushButton(self.layoutWidget)
        self.btn_voltar_devolv.setObjectName(u"btn_voltar_devolv")
        self.btn_voltar_devolv.setMinimumSize(QSize(0, 25))
        self.btn_voltar_devolv.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout.addWidget(self.btn_voltar_devolv)

        self.btn_devolv = QPushButton(self.layoutWidget)
        self.btn_devolv.setObjectName(u"btn_devolv")
        self.btn_devolv.setMinimumSize(QSize(0, 25))
        self.btn_devolv.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout.addWidget(self.btn_devolv)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.retranslateUi(WinDevol)

        QMetaObject.connectSlotsByName(WinDevol)
    # setupUi

    def retranslateUi(self, WinDevol):
        WinDevol.setWindowTitle(QCoreApplication.translate("WinDevol", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("WinDevol", u"Devolver Ferramenta", None))
        self.label_2.setText(QCoreApplication.translate("WinDevol", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Digite o C\u00f3digo da Ferramenta:</span></p></body></html>", None))
        self.label_3.setText("")
        self.btn_voltar_devolv.setText(QCoreApplication.translate("WinDevol", u"Voltar", None))
        self.btn_devolv.setText(QCoreApplication.translate("WinDevol", u"Devolver", None))
        self.label_4.setText("")
        self.label_5.setText("")
    # retranslateUi

