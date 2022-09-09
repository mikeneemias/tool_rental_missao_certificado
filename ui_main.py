# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 508)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(613, 508))
        MainWindow.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 16px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}\n"
"")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 30))
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 16px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}\n"
"")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 16px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout.addWidget(self.btn_sobre)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setStyleSheet(u"background-color:rgb(31, 31, 31)")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color:rgba(25,25,25,255)")

        self.verticalLayout.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_tabelas = QWidget()
        self.pg_tabelas.setObjectName(u"pg_tabelas")
        self.pg_tabelas.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.verticalLayout_3 = QVBoxLayout(self.pg_tabelas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabelas = QTabWidget(self.pg_tabelas)
        self.tabelas.setObjectName(u"tabelas")
        self.tabelas.setMinimumSize(QSize(561, 312))
        self.tabelas.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.aba_ferramentas = QWidget()
        self.aba_ferramentas.setObjectName(u"aba_ferramentas")
        sizePolicy.setHeightForWidth(self.aba_ferramentas.sizePolicy().hasHeightForWidth())
        self.aba_ferramentas.setSizePolicy(sizePolicy)
        self.aba_ferramentas.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.layoutWidget = QWidget(self.aba_ferramentas)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 577, 389))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabela_ferramentas = QTableView(self.layoutWidget)
        self.tabela_ferramentas.setObjectName(u"tabela_ferramentas")
        self.tabela_ferramentas.setMinimumSize(QSize(567, 308))

        self.verticalLayout_5.addWidget(self.tabela_ferramentas)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(561, 73))
        self.frame_4.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_nova_ferramenta = QPushButton(self.frame_4)
        self.btn_nova_ferramenta.setObjectName(u"btn_nova_ferramenta")
        self.btn_nova_ferramenta.setMinimumSize(QSize(0, 25))
        self.btn_nova_ferramenta.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_2.addWidget(self.btn_nova_ferramenta)

        self.btn_excluir_ferramenta = QPushButton(self.frame_4)
        self.btn_excluir_ferramenta.setObjectName(u"btn_excluir_ferramenta")
        self.btn_excluir_ferramenta.setMinimumSize(QSize(0, 25))
        self.btn_excluir_ferramenta.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_2.addWidget(self.btn_excluir_ferramenta)

        self.btn_exportar_ferramenta = QPushButton(self.frame_4)
        self.btn_exportar_ferramenta.setObjectName(u"btn_exportar_ferramenta")
        self.btn_exportar_ferramenta.setMinimumSize(QSize(0, 25))
        self.btn_exportar_ferramenta.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_2.addWidget(self.btn_exportar_ferramenta)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.tabelas.addTab(self.aba_ferramentas, "")
        self.aba_tecnicos = QWidget()
        self.aba_tecnicos.setObjectName(u"aba_tecnicos")
        sizePolicy.setHeightForWidth(self.aba_tecnicos.sizePolicy().hasHeightForWidth())
        self.aba_tecnicos.setSizePolicy(sizePolicy)
        self.aba_tecnicos.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.layoutWidget1 = QWidget(self.aba_tecnicos)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 571, 389))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabela_tecnicos = QTableView(self.layoutWidget1)
        self.tabela_tecnicos.setObjectName(u"tabela_tecnicos")
        self.tabela_tecnicos.setMinimumSize(QSize(567, 308))

        self.verticalLayout_7.addWidget(self.tabela_tecnicos)

        self.frame_3 = QFrame(self.layoutWidget1)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(561, 73))
        self.frame_3.setStyleSheet(u"background-color:rgba(25, 25, 25,255)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_novo_tecnico = QPushButton(self.frame_3)
        self.btn_novo_tecnico.setObjectName(u"btn_novo_tecnico")
        self.btn_novo_tecnico.setMinimumSize(QSize(0, 25))
        self.btn_novo_tecnico.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_3.addWidget(self.btn_novo_tecnico)

        self.btn_excluir_tecnico = QPushButton(self.frame_3)
        self.btn_excluir_tecnico.setObjectName(u"btn_excluir_tecnico")
        self.btn_excluir_tecnico.setMinimumSize(QSize(0, 25))
        self.btn_excluir_tecnico.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_3.addWidget(self.btn_excluir_tecnico)

        self.btn_exportar_tecnicos = QPushButton(self.frame_3)
        self.btn_exportar_tecnicos.setObjectName(u"btn_exportar_tecnicos")
        self.btn_exportar_tecnicos.setMinimumSize(QSize(0, 25))
        self.btn_exportar_tecnicos.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_3.addWidget(self.btn_exportar_tecnicos)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.tabelas.addTab(self.aba_tecnicos, "")
        self.aba_reservas = QWidget()
        self.aba_reservas.setObjectName(u"aba_reservas")
        self.aba_reservas.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.tabela_reservas = QTableView(self.aba_reservas)
        self.tabela_reservas.setObjectName(u"tabela_reservas")
        self.tabela_reservas.setGeometry(QRect(1, 1, 567, 308))
        self.tabela_reservas.setMinimumSize(QSize(567, 308))
        self.frame_2 = QFrame(self.aba_reservas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1, 315, 561, 73))
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(561, 73))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_nova_reserva = QPushButton(self.frame_2)
        self.btn_nova_reserva.setObjectName(u"btn_nova_reserva")
        self.btn_nova_reserva.setMinimumSize(QSize(0, 25))
        self.btn_nova_reserva.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_4.addWidget(self.btn_nova_reserva)

        self.btn_finalizar_reserva = QPushButton(self.frame_2)
        self.btn_finalizar_reserva.setObjectName(u"btn_finalizar_reserva")
        self.btn_finalizar_reserva.setMinimumSize(QSize(0, 25))
        self.btn_finalizar_reserva.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_4.addWidget(self.btn_finalizar_reserva)

        self.btn_exportar_reservas = QPushButton(self.frame_2)
        self.btn_exportar_reservas.setObjectName(u"btn_exportar_reservas")
        self.btn_exportar_reservas.setMinimumSize(QSize(0, 25))
        self.btn_exportar_reservas.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_4.addWidget(self.btn_exportar_reservas)

        self.tabelas.addTab(self.aba_reservas, "")

        self.verticalLayout_3.addWidget(self.tabelas)

        self.Pages.addWidget(self.pg_tabelas)
        self.pg_cadastro_ferramentas = QWidget()
        self.pg_cadastro_ferramentas.setObjectName(u"pg_cadastro_ferramentas")
        self.pg_cadastro_ferramentas.setMinimumSize(QSize(595, 436))
        self.pg_cadastro_ferramentas.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.verticalLayout_4 = QVBoxLayout(self.pg_cadastro_ferramentas)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.pg_cadastro_ferramentas)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setMargin(-1)
        self.label_15.setIndent(-2)

        self.verticalLayout_4.addWidget(self.label_15)

        self.label_3 = QLabel(self.pg_cadastro_ferramentas)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.pg_cadastro_ferramentas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(119, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.txt_descricao = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setMinimumSize(QSize(450, 20))
        self.txt_descricao.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_descricao.setMaxLength(60)

        self.horizontalLayout_5.addWidget(self.txt_descricao)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.pg_cadastro_ferramentas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(119, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.txt_fabricante = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_fabricante.setObjectName(u"txt_fabricante")
        self.txt_fabricante.setMinimumSize(QSize(450, 20))
        self.txt_fabricante.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_fabricante.setMaxLength(30)

        self.horizontalLayout_6.addWidget(self.txt_fabricante)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.pg_cadastro_ferramentas)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(119, 0))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.txt_voltagem = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_voltagem.setObjectName(u"txt_voltagem")
        self.txt_voltagem.setMinimumSize(QSize(450, 20))
        self.txt_voltagem.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_voltagem.setMaxLength(15)

        self.horizontalLayout_7.addWidget(self.txt_voltagem)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.pg_cadastro_ferramentas)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(119, 0))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.txt_part_numb = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_part_numb.setObjectName(u"txt_part_numb")
        self.txt_part_numb.setMinimumSize(QSize(450, 20))
        self.txt_part_numb.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_part_numb.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhLatinOnly)
        self.txt_part_numb.setMaxLength(25)

        self.horizontalLayout_8.addWidget(self.txt_part_numb)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.pg_cadastro_ferramentas)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(119, 0))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.txt_tamanho = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_tamanho.setObjectName(u"txt_tamanho")
        self.txt_tamanho.setMinimumSize(QSize(450, 20))
        self.txt_tamanho.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_tamanho.setMaxLength(20)

        self.horizontalLayout_9.addWidget(self.txt_tamanho)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.pg_cadastro_ferramentas)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(119, 0))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.txt_un_medida = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_un_medida.setObjectName(u"txt_un_medida")
        self.txt_un_medida.setMinimumSize(QSize(450, 20))
        self.txt_un_medida.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_un_medida.setMaxLength(15)

        self.horizontalLayout_10.addWidget(self.txt_un_medida)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.pg_cadastro_ferramentas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(119, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.txt_tipo = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_tipo.setObjectName(u"txt_tipo")
        self.txt_tipo.setMinimumSize(QSize(450, 20))
        self.txt_tipo.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_tipo.setMaxLength(15)

        self.horizontalLayout_11.addWidget(self.txt_tipo)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.pg_cadastro_ferramentas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(119, 0))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_7)

        self.txt_material = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_material.setObjectName(u"txt_material")
        self.txt_material.setMinimumSize(QSize(450, 20))
        self.txt_material.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_material.setMaxLength(15)

        self.horizontalLayout_12.addWidget(self.txt_material)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.pg_cadastro_ferramentas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(119, 0))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_8)

        self.txt_horas = QLineEdit(self.pg_cadastro_ferramentas)
        self.txt_horas.setObjectName(u"txt_horas")
        self.txt_horas.setMinimumSize(QSize(450, 20))
        self.txt_horas.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_horas.setInputMethodHints(Qt.ImhDigitsOnly)
        self.txt_horas.setMaxLength(3)

        self.horizontalLayout_13.addWidget(self.txt_horas)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.pg_cadastro_ferramentas)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.btn_cadastrar_ferramenta = QPushButton(self.pg_cadastro_ferramentas)
        self.btn_cadastrar_ferramenta.setObjectName(u"btn_cadastrar_ferramenta")
        self.btn_cadastrar_ferramenta.setMinimumSize(QSize(0, 25))
        self.btn_cadastrar_ferramenta.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_14.addWidget(self.btn_cadastrar_ferramenta)

        self.btn_voltar_ferramenta = QPushButton(self.pg_cadastro_ferramentas)
        self.btn_voltar_ferramenta.setObjectName(u"btn_voltar_ferramenta")
        self.btn_voltar_ferramenta.setMinimumSize(QSize(0, 25))
        self.btn_voltar_ferramenta.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_14.addWidget(self.btn_voltar_ferramenta)

        self.label_9 = QLabel(self.pg_cadastro_ferramentas)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.Pages.addWidget(self.pg_cadastro_ferramentas)
        self.pg_cadastro_tecnicos = QWidget()
        self.pg_cadastro_tecnicos.setObjectName(u"pg_cadastro_tecnicos")
        self.pg_cadastro_tecnicos.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro_tecnicos)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.pg_cadastro_tecnicos)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setMargin(-1)
        self.label_16.setIndent(-2)

        self.verticalLayout_8.addWidget(self.label_16)

        self.label_22 = QLabel(self.pg_cadastro_tecnicos)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_22)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.pg_cadastro_tecnicos)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(119, 0))
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_20)

        self.txt_nome = QLineEdit(self.pg_cadastro_tecnicos)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(450, 25))
        self.txt_nome.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_nome.setMaxLength(40)

        self.horizontalLayout_17.addWidget(self.txt_nome)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_23 = QLabel(self.pg_cadastro_tecnicos)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(119, 0))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_23)

        self.txt_cpf = QLineEdit(self.pg_cadastro_tecnicos)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setMinimumSize(QSize(450, 25))
        self.txt_cpf.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_cpf.setInputMethodHints(Qt.ImhPreferNumbers)
        self.txt_cpf.setMaxLength(11)

        self.horizontalLayout_19.addWidget(self.txt_cpf)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_27 = QLabel(self.pg_cadastro_tecnicos)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(119, 0))
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_27)

        self.txt_telefone = QLineEdit(self.pg_cadastro_tecnicos)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setMinimumSize(QSize(450, 25))
        self.txt_telefone.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_telefone.setInputMethodHints(Qt.ImhPreferNumbers)
        self.txt_telefone.setMaxLength(9)

        self.horizontalLayout_23.addWidget(self.txt_telefone)


        self.verticalLayout_8.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.pg_cadastro_tecnicos)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(119, 0))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_19)

        self.txt_turno = QComboBox(self.pg_cadastro_tecnicos)
        self.txt_turno.addItem("")
        self.txt_turno.addItem("")
        self.txt_turno.addItem("")
        self.txt_turno.addItem("")
        self.txt_turno.addItem("")
        self.txt_turno.setObjectName(u"txt_turno")
        self.txt_turno.setMinimumSize(QSize(450, 25))
        self.txt_turno.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"border:1px solid white;\n"
"background-color:rgba(25, 25, 25, 255);\n"
"font-family:Trebuchet MS;\n"
"font-size:11px;")

        self.horizontalLayout_16.addWidget(self.txt_turno)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_26 = QLabel(self.pg_cadastro_tecnicos)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(119, 0))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_26)

        self.txt_nome_equipe = QLineEdit(self.pg_cadastro_tecnicos)
        self.txt_nome_equipe.setObjectName(u"txt_nome_equipe")
        self.txt_nome_equipe.setMinimumSize(QSize(450, 25))
        self.txt_nome_equipe.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_nome_equipe.setMaxLength(30)

        self.horizontalLayout_22.addWidget(self.txt_nome_equipe)


        self.verticalLayout_8.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.pg_cadastro_tecnicos)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.btn_cadastrar_tecnico = QPushButton(self.pg_cadastro_tecnicos)
        self.btn_cadastrar_tecnico.setObjectName(u"btn_cadastrar_tecnico")
        self.btn_cadastrar_tecnico.setMinimumSize(QSize(0, 25))
        self.btn_cadastrar_tecnico.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_15.addWidget(self.btn_cadastrar_tecnico)

        self.label_18 = QLabel(self.pg_cadastro_tecnicos)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_15.addWidget(self.label_18)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_24 = QLabel(self.pg_cadastro_tecnicos)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_18.addWidget(self.label_24)

        self.btn_voltar_tecnico = QPushButton(self.pg_cadastro_tecnicos)
        self.btn_voltar_tecnico.setObjectName(u"btn_voltar_tecnico")
        self.btn_voltar_tecnico.setMinimumSize(QSize(0, 25))
        self.btn_voltar_tecnico.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}\n"
"")

        self.horizontalLayout_18.addWidget(self.btn_voltar_tecnico)

        self.label_25 = QLabel(self.pg_cadastro_tecnicos)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_18.addWidget(self.label_25)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.Pages.addWidget(self.pg_cadastro_tecnicos)
        self.pg_nova_reserva = QWidget()
        self.pg_nova_reserva.setObjectName(u"pg_nova_reserva")
        self.pg_nova_reserva.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.verticalLayout_9 = QVBoxLayout(self.pg_nova_reserva)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_21 = QLabel(self.pg_nova_reserva)
        self.label_21.setObjectName(u"label_21")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_21)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.id_ferramenta = QLabel(self.pg_nova_reserva)
        self.id_ferramenta.setObjectName(u"id_ferramenta")
        self.id_ferramenta.setMinimumSize(QSize(140, 0))
        self.id_ferramenta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.id_ferramenta)

        self.txt_codigo = QLineEdit(self.pg_nova_reserva)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setMinimumSize(QSize(430, 20))
        self.txt_codigo.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_codigo.setInputMethodHints(Qt.ImhDigitsOnly)
        self.txt_codigo.setMaxLength(6)

        self.horizontalLayout_21.addWidget(self.txt_codigo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.descricao_reserva = QLabel(self.pg_nova_reserva)
        self.descricao_reserva.setObjectName(u"descricao_reserva")
        self.descricao_reserva.setMinimumSize(QSize(140, 0))
        self.descricao_reserva.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.descricao_reserva)

        self.txt_solicitacao = QLineEdit(self.pg_nova_reserva)
        self.txt_solicitacao.setObjectName(u"txt_solicitacao")
        self.txt_solicitacao.setMinimumSize(QSize(430, 20))
        self.txt_solicitacao.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_solicitacao.setMaxLength(60)

        self.horizontalLayout_24.addWidget(self.txt_solicitacao)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.data_retirada = QLabel(self.pg_nova_reserva)
        self.data_retirada.setObjectName(u"data_retirada")
        self.data_retirada.setMinimumSize(QSize(140, 0))
        self.data_retirada.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.data_retirada)

        self.txt_data_retirada = QDateTimeEdit(self.pg_nova_reserva)
        self.txt_data_retirada.setObjectName(u"txt_data_retirada")
        self.txt_data_retirada.setMinimumSize(QSize(430, 20))
        self.txt_data_retirada.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"border:1px solid white;\n"
"background-color:rgba(25, 25, 25, 255);\n"
"font-family:Trebuchet MS;\n"
"font-size:11px;")
        self.txt_data_retirada.setInputMethodHints(Qt.ImhNone)
        self.txt_data_retirada.setDate(QDate(2022, 1, 1))
        self.txt_data_retirada.setMinimumDate(QDate(2022, 1, 1))
        self.txt_data_retirada.setCalendarPopup(True)

        self.horizontalLayout_25.addWidget(self.txt_data_retirada)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.data_devolucao = QLabel(self.pg_nova_reserva)
        self.data_devolucao.setObjectName(u"data_devolucao")
        self.data_devolucao.setMinimumSize(QSize(140, 0))
        self.data_devolucao.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.data_devolucao)

        self.txt_data_dev = QDateTimeEdit(self.pg_nova_reserva)
        self.txt_data_dev.setObjectName(u"txt_data_dev")
        self.txt_data_dev.setMinimumSize(QSize(430, 20))
        self.txt_data_dev.setStyleSheet(u"color:rgba(255,255,255,1);\n"
"border:1px solid white;\n"
"background-color:rgba(25, 25, 25, 255);\n"
"font-family:Trebuchet MS;\n"
"font-size:11px;")
        self.txt_data_dev.setMinimumDate(QDate(2022, 1, 1))
        self.txt_data_dev.setMaximumTime(QTime(23, 59, 59))
        self.txt_data_dev.setCalendarPopup(True)

        self.horizontalLayout_26.addWidget(self.txt_data_dev)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.tecnico_reserva = QLabel(self.pg_nova_reserva)
        self.tecnico_reserva.setObjectName(u"tecnico_reserva")
        self.tecnico_reserva.setMinimumSize(QSize(140, 0))
        self.tecnico_reserva.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.tecnico_reserva)

        self.txt_cod_tecnico_reserva = QLineEdit(self.pg_nova_reserva)
        self.txt_cod_tecnico_reserva.setObjectName(u"txt_cod_tecnico_reserva")
        self.txt_cod_tecnico_reserva.setMinimumSize(QSize(430, 20))
        self.txt_cod_tecnico_reserva.setStyleSheet(u"color:rgb(255,255,255)")
        self.txt_cod_tecnico_reserva.setMaxLength(40)

        self.horizontalLayout_27.addWidget(self.txt_cod_tecnico_reserva)


        self.verticalLayout_9.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_31 = QLabel(self.pg_nova_reserva)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_28.addWidget(self.label_31)

        self.btn_reservar_feramenta = QPushButton(self.pg_nova_reserva)
        self.btn_reservar_feramenta.setObjectName(u"btn_reservar_feramenta")
        self.btn_reservar_feramenta.setMinimumSize(QSize(0, 25))
        self.btn_reservar_feramenta.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_28.addWidget(self.btn_reservar_feramenta)

        self.btn_voltar_reserva = QPushButton(self.pg_nova_reserva)
        self.btn_voltar_reserva.setObjectName(u"btn_voltar_reserva")
        self.btn_voltar_reserva.setMinimumSize(QSize(0, 25))
        self.btn_voltar_reserva.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	background-color:rgba(59,59,59,255);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgba(77,77,77,255); color:white}")

        self.horizontalLayout_28.addWidget(self.btn_voltar_reserva)

        self.label_32 = QLabel(self.pg_nova_reserva)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_28.addWidget(self.label_32)


        self.verticalLayout_9.addLayout(self.horizontalLayout_28)

        self.Pages.addWidget(self.pg_nova_reserva)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pg_sobre.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.label_2 = QLabel(self.pg_sobre)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(16, 12, 561, 291))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(561, 291))
        self.label_2.setStyleSheet(u"background-color:rgba(25,25,25,255)")
        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabelas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Tabelas", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Miss\u00e3o Certificado - Mundo 1</span><span style=\" color:#ffffff;\"><br/><br/></span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Aluguel de Ferramentas</span></p></body></html>", None))
        self.btn_nova_ferramenta.setText(QCoreApplication.translate("MainWindow", u"Nova Ferramenta", None))
        self.btn_excluir_ferramenta.setText(QCoreApplication.translate("MainWindow", u"Excluir Ferramenta", None))
        self.btn_exportar_ferramenta.setText(QCoreApplication.translate("MainWindow", u"Exportar para Excel", None))
        self.tabelas.setTabText(self.tabelas.indexOf(self.aba_ferramentas), QCoreApplication.translate("MainWindow", u"Ferramentas", None))
        self.btn_novo_tecnico.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Novo T\u00e9cnico", None))
        self.btn_excluir_tecnico.setText(QCoreApplication.translate("MainWindow", u"Excluir Cadastro", None))
        self.btn_exportar_tecnicos.setText(QCoreApplication.translate("MainWindow", u"Exportar para Excel", None))
        self.tabelas.setTabText(self.tabelas.indexOf(self.aba_tecnicos), QCoreApplication.translate("MainWindow", u"T\u00e9cnicos", None))
        self.btn_nova_reserva.setText(QCoreApplication.translate("MainWindow", u"Nova Reserva", None))
        self.btn_finalizar_reserva.setText(QCoreApplication.translate("MainWindow", u"Entregar Ferramenta", None))
        self.btn_exportar_reservas.setText(QCoreApplication.translate("MainWindow", u"Exportar para Excel", None))
        self.tabelas.setTabText(self.tabelas.indexOf(self.aba_reservas), QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Tela de Cadastro</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#fdfdfd;\">Cadastrar Ferramenta</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Descri\u00e7\u00e3o</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Fabricante</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Voltagem</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Part Number</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Tamanho</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Unidade de Medida</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Tipo</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Material</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Tempo Reserva (h)</span></p></body></html>", None))
        self.label_14.setText("")
        self.btn_cadastrar_ferramenta.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_voltar_ferramenta.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_9.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#fefefe;\">Tela de Cadastro</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Cadastrar T\u00e9cnico</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Nome Completo</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">CPF</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Telefone</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Turno</span></p></body></html>", None))
        self.txt_turno.setItemText(0, "")
        self.txt_turno.setItemText(1, QCoreApplication.translate("MainWindow", u"Selecione uma op\u00e7\u00e3o", None))
        self.txt_turno.setItemText(2, QCoreApplication.translate("MainWindow", u"Manh\u00e3", None))
        self.txt_turno.setItemText(3, QCoreApplication.translate("MainWindow", u"Tarde", None))
        self.txt_turno.setItemText(4, QCoreApplication.translate("MainWindow", u"Noite", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Nome da equipe</span></p></body></html>", None))
        self.label_17.setText("")
        self.btn_cadastrar_tecnico.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_18.setText("")
        self.label_24.setText("")
        self.btn_voltar_tecnico.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_25.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Reservar Ferramenta</span></p></body></html>", None))
        self.id_ferramenta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">C\u00f3digo da Ferramenta</span></p></body></html>", None))
        self.descricao_reserva.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Descri\u00e7\u00e3o</span></p></body></html>", None))
        self.data_retirada.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Data da retirada</span></p></body></html>", None))
        self.data_devolucao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Data da devolu\u00e7\u00e3o</span></p></body></html>", None))
        self.tecnico_reserva.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">C\u00f3digo do t\u00e9cnico:</span></p></body></html>", None))
        self.label_31.setText("")
        self.btn_reservar_feramenta.setText(QCoreApplication.translate("MainWindow", u"Reservar", None))
        self.btn_voltar_reserva.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_32.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">DEV TEAM 15 - </span><span style=\" font-size:16pt; color:#ffffff;\">2022.2</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ANA JULIA BENEDETTI</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">MAT - 202204478366</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">MIQU\u00c9IAS NEEMIAS MATIAS MARTINS</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">MAT - 202205084094</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
    # retranslateUi

