# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowgenerico.ui'
#
# Created: Mon Nov 24 22:25:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from scripts.generico.ui_generico_eabrirserial import Ui_ui_GENERICO_eAbrirSerial
from scripts.generico.ui_generico_rreceberdados import Ui_ui_GENERICO_rReceberDados
from scripts.generico.ui_generico_tenviardados import Ui_ui_GENERICO_tEnviarDados
from scripts.ui_geral_contatossuporte import Ui_ui_Geral_ContatosSuporte


class Ui_MainWindowGenerico(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindowGenerico, self).__init__()

        self.setupUi(self)
        self.pushButtonGenericoEncerrar.clicked.connect(self.on_pushButtonEncerrar_clicked)
        self.pushButtonGenericoContatos.clicked.connect(self.on_pushButtonContatos_clicked)
        self.actionEAbrirSerial_Daruma.triggered.connect(self.on_actionEAbrirSerial_Daruma_triggered)
        self.actionTEnviarDados_Daruma.triggered.connect(self.on_actionTEnviarDados_Daruma_triggered)
        self.actionRReceberDados_Daruma.triggered.connect(self.on_actionRReceberDados_Daruma_triggered)
        self.actionEFecharSerial_Daruma.triggered.connect(self.actionEFecharSerial_Daruma_triggered)

    def on_pushButtonEncerrar_clicked(self):
        self.close()

    def on_pushButtonContatos_clicked(self):
        self.form_Geral_ContatosSuporte = Ui_ui_Geral_ContatosSuporte();
        self.form_Geral_ContatosSuporte.show()

    def on_actionEAbrirSerial_Daruma_triggered(self):
        self.form_GENERICO_eAbrirSerial = Ui_ui_GENERICO_eAbrirSerial();
        self.form_GENERICO_eAbrirSerial.show()

    def on_actionTEnviarDados_Daruma_triggered(self):
        self.form_GENERICO_tEnviarDados = Ui_ui_GENERICO_tEnviarDados();
        self.form_GENERICO_tEnviarDados.show()

    def on_actionRReceberDados_Daruma_triggered(self):
        self.form_GENERICO_rReceberDados = Ui_ui_GENERICO_rReceberDados();
        self.form_GENERICO_rReceberDados.show()
        pass

    def actionEFecharSerial_Daruma_triggered(self):
        pass

    def setupUi(self, MainWindowGenerico):
        MainWindowGenerico.setObjectName("MainWindowGenerico")
        MainWindowGenerico.resize(823, 454)
        MainWindowGenerico.setMaximumSize(QtCore.QSize(823, 454))
        self.centralwidget = QtGui.QWidget(MainWindowGenerico)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 159, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 167))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(1, 144, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(195, 87))
        self.label_4.setMaximumSize(QtCore.QSize(195, 87))
        self.label_4.setStyleSheet("background-image: url(:/Recursos/Imagens/logo_daruma_developers.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(1, 144, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonGenericoContatos = QtGui.QPushButton(self.frame)
        self.pushButtonGenericoContatos.setMinimumSize(QtCore.QSize(191, 101))
        self.pushButtonGenericoContatos.setMaximumSize(QtCore.QSize(191, 101))
        self.pushButtonGenericoContatos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonGenericoContatos.setStyleSheet("background-image: url(:/Recursos/Imagens/avatar.png);")
        self.pushButtonGenericoContatos.setText("")
        self.pushButtonGenericoContatos.setObjectName("pushButtonGenericoContatos")
        self.horizontalLayout_3.addWidget(self.pushButtonGenericoContatos)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButtonGenericoEncerrar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonGenericoEncerrar.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButtonGenericoEncerrar.setObjectName("pushButtonGenericoEncerrar")
        self.horizontalLayout_4.addWidget(self.pushButtonGenericoEncerrar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindowGenerico.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowGenerico)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbrir_Porta_de_Comunica_o = QtGui.QMenu(self.menubar)
        self.menuAbrir_Porta_de_Comunica_o.setObjectName("menuAbrir_Porta_de_Comunica_o")
        self.menuEnviar_Dados = QtGui.QMenu(self.menubar)
        self.menuEnviar_Dados.setObjectName("menuEnviar_Dados")
        self.menuReceber_Dados = QtGui.QMenu(self.menubar)
        self.menuReceber_Dados.setObjectName("menuReceber_Dados")
        self.menuFechar_Porta_de_Comunica_o = QtGui.QMenu(self.menubar)
        self.menuFechar_Porta_de_Comunica_o.setObjectName("menuFechar_Porta_de_Comunica_o")
        MainWindowGenerico.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowGenerico)
        self.statusbar.setObjectName("statusbar")
        MainWindowGenerico.setStatusBar(self.statusbar)
        self.actionEAbrirSerial_Daruma = QtGui.QAction(MainWindowGenerico)
        self.actionEAbrirSerial_Daruma.setObjectName("actionEAbrirSerial_Daruma")
        self.actionTEnviarDados_Daruma = QtGui.QAction(MainWindowGenerico)
        self.actionTEnviarDados_Daruma.setObjectName("actionTEnviarDados_Daruma")
        self.actionRReceberDados_Daruma = QtGui.QAction(MainWindowGenerico)
        self.actionRReceberDados_Daruma.setObjectName("actionRReceberDados_Daruma")
        self.actionEFecharSerial_Daruma = QtGui.QAction(MainWindowGenerico)
        self.actionEFecharSerial_Daruma.setObjectName("actionEFecharSerial_Daruma")
        self.menuAbrir_Porta_de_Comunica_o.addAction(self.actionEAbrirSerial_Daruma)
        self.menuEnviar_Dados.addAction(self.actionTEnviarDados_Daruma)
        self.menuReceber_Dados.addAction(self.actionRReceberDados_Daruma)
        self.menuFechar_Porta_de_Comunica_o.addAction(self.actionEFecharSerial_Daruma)
        self.menubar.addAction(self.menuAbrir_Porta_de_Comunica_o.menuAction())
        self.menubar.addAction(self.menuEnviar_Dados.menuAction())
        self.menubar.addAction(self.menuReceber_Dados.menuAction())
        self.menubar.addAction(self.menuFechar_Porta_de_Comunica_o.menuAction())

        self.retranslateUi(MainWindowGenerico)
        QtCore.QMetaObject.connectSlotsByName(MainWindowGenerico)

    def retranslateUi(self, MainWindowGenerico):
        MainWindowGenerico.setWindowTitle(QtGui.QApplication.translate("MainWindowGenerico", "Módulo Genérico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindowGenerico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Dúvidas? Ligue: 0800 77 0332 0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindowGenerico", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Genérico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">(pode ser usado com qualquer produto)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; font-weight:600;\">Driver: DarumaFramework</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGenericoEncerrar.setText(QtGui.QApplication.translate("MainWindowGenerico", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbrir_Porta_de_Comunica_o.setTitle(QtGui.QApplication.translate("MainWindowGenerico", "Abrir Porta de Comunicação", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEnviar_Dados.setTitle(QtGui.QApplication.translate("MainWindowGenerico", "Enviar Dados", None, QtGui.QApplication.UnicodeUTF8))
        self.menuReceber_Dados.setTitle(QtGui.QApplication.translate("MainWindowGenerico", "Receber Dados", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFechar_Porta_de_Comunica_o.setTitle(QtGui.QApplication.translate("MainWindowGenerico", "Fechar Porta de Comunicação", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEAbrirSerial_Daruma.setText(QtGui.QApplication.translate("MainWindowGenerico", "eAbrirSerial_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTEnviarDados_Daruma.setText(QtGui.QApplication.translate("MainWindowGenerico", "tEnviarDados_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRReceberDados_Daruma.setText(QtGui.QApplication.translate("MainWindowGenerico", "rReceberDados_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEFecharSerial_Daruma.setText(QtGui.QApplication.translate("MainWindowGenerico", "eFecharSerial_Daruma", None, QtGui.QApplication.UnicodeUTF8))

