# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgetprincipal.ui'
#
# Created: Mon Nov 24 22:26:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QUrl
from PySide.QtGui import QDesktopServices
from scripts.dual.mainwindowdual import Ui_MainWindowDual
from scripts.fiscal.mainwindowfiscal import Ui_MainWindowFISCAL
from scripts.generico.mainwindowgenerico import Ui_MainWindowGenerico
from scripts.modem.mainwindowmodem import Ui_MainWindowModem
import Recursos_rc

class Ui_WidgetPrincipal(QtGui.QWidget):

    def __init__(self):
        super(Ui_WidgetPrincipal, self).__init__()

        self.setupUi(self)

        self.pushButtonImpressoraFiscal.clicked.connect(self.on_pushButtonImpressoraFiscal_clicked)
        self.pushButtonImpressoraDual.clicked.connect(self.on_pushButtonImpressoraDual_clicked)
        self.pushButtonGenerico.clicked.connect(self.on_pushButtonGenerico_clicked)
        self.pushButtonImpressoraModem.clicked.connect(self.on_pushButtonImpressoraModem_clicked)
        self.pushButtonFechar.clicked.connect(self.close)
        self.pushButtonHelpOnline.clicked.connect(self.on_pushButtonHelpOnline_clicked)

    def on_pushButtonImpressoraFiscal_clicked(self):
        self.formPrincipalECF = Ui_MainWindowFISCAL()
        self.formPrincipalECF.showMaximized()

    def on_pushButtonImpressoraDual_clicked(self):
        self.formPrincipalDual = Ui_MainWindowDual();
        self.formPrincipalDual.showMaximized();

    def on_pushButtonHelpOnline_clicked(self):
        QDesktopServices.openUrl(QUrl("http://desenvolvedoresdaruma.com.br/home/downloads/Site_2011/Help/DarumaFrameworkHelpOnline/Daruma_Framework.htm"));

    def on_pushButtonGenerico_clicked(self):
        self.formPrincipalGenerico = Ui_MainWindowGenerico();
        self.formPrincipalGenerico.showMaximized();

    def on_pushButtonFechar_clicked(self):
        self.close()

    def on_pushButtonImpressoraModem_clicked(self):
        self.formPrincipalModem = Ui_MainWindowModem();
        self.formPrincipalModem.showMaximized();

    def setupUi(self, WidgetPrincipal):
        WidgetPrincipal.setObjectName("WidgetPrincipal")
        WidgetPrincipal.setEnabled(True)
        WidgetPrincipal.resize(696, 313)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetPrincipal.sizePolicy().hasHeightForWidth())
        WidgetPrincipal.setSizePolicy(sizePolicy)
        WidgetPrincipal.setMinimumSize(QtCore.QSize(696, 313))
        WidgetPrincipal.setMaximumSize(QtCore.QSize(696, 313))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Recursos/Imagens/logo_daruma_developers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WidgetPrincipal.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(WidgetPrincipal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(WidgetPrincipal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtGui.QGroupBox(WidgetPrincipal)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(131, 121))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonImpressoraFiscal = QtGui.QPushButton(self.groupBox)
        self.pushButtonImpressoraFiscal.setEnabled(True)
        self.pushButtonImpressoraFiscal.setMinimumSize(QtCore.QSize(111, 61))
        self.pushButtonImpressoraFiscal.setObjectName("pushButtonImpressoraFiscal")
        self.gridLayout.addWidget(self.pushButtonImpressoraFiscal, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(WidgetPrincipal)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setMinimumSize(QtCore.QSize(131, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonImpressoraDual = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonImpressoraDual.setEnabled(True)
        self.pushButtonImpressoraDual.setMinimumSize(QtCore.QSize(111, 61))
        self.pushButtonImpressoraDual.setObjectName("pushButtonImpressoraDual")
        self.gridLayout_2.addWidget(self.pushButtonImpressoraDual, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(WidgetPrincipal)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setMinimumSize(QtCore.QSize(131, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonImpressoraModem = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonImpressoraModem.setEnabled(True)
        self.pushButtonImpressoraModem.setMinimumSize(QtCore.QSize(111, 61))
        self.pushButtonImpressoraModem.setCheckable(True)
        self.pushButtonImpressoraModem.setObjectName("pushButtonImpressoraModem")
        self.gridLayout_3.addWidget(self.pushButtonImpressoraModem, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_5 = QtGui.QGroupBox(WidgetPrincipal)
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setMinimumSize(QtCore.QSize(131, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonGenerico = QtGui.QPushButton(self.groupBox_5)
        self.pushButtonGenerico.setMinimumSize(QtCore.QSize(11, 61))
        self.pushButtonGenerico.setObjectName("pushButtonGenerico")
        self.gridLayout_4.addWidget(self.pushButtonGenerico, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonHelpOnline = QtGui.QPushButton(WidgetPrincipal)
        self.pushButtonHelpOnline.setObjectName("pushButtonHelpOnline")
        self.horizontalLayout_4.addWidget(self.pushButtonHelpOnline)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButtonFechar = QtGui.QPushButton(WidgetPrincipal)
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.horizontalLayout_4.addWidget(self.pushButtonFechar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(WidgetPrincipal)
        QtCore.QMetaObject.connectSlotsByName(WidgetPrincipal)

    def retranslateUi(self, WidgetPrincipal):
        WidgetPrincipal.setWindowTitle(QtGui.QApplication.translate("WidgetPrincipal", "DarumaFrameWork - Exemplo em Python - Urmet Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WidgetPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Daruma Framework</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt;\">Exemplo em Python 3.4.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt;\">QtCreator: 2.2.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana\'; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt;\">Versão: 0.0.1</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WidgetPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Recursos/Imagens/logo_daruma_developers.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WidgetPrincipal", "FISCAL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImpressoraFiscal.setText(QtGui.QApplication.translate("WidgetPrincipal", "Impressora FISCAL", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("WidgetPrincipal", "NÃO FISCAL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImpressoraDual.setText(QtGui.QApplication.translate("WidgetPrincipal", "Impressora DUAL", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("WidgetPrincipal", "MODEM", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImpressoraModem.setText(QtGui.QApplication.translate("WidgetPrincipal", "MODEM", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("WidgetPrincipal", "GENÉRICO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGenerico.setText(QtGui.QApplication.translate("WidgetPrincipal", "GENÉRICO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonHelpOnline.setText(QtGui.QApplication.translate("WidgetPrincipal", "Help Online", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("WidgetPrincipal", "Fechar Aplicação", None, QtGui.QApplication.UnicodeUTF8))
