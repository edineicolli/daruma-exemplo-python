# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geral_contatossuporte.ui'
#
# Created: Mon Nov 24 22:26:40 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_Geral_ContatosSuporte(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_Geral_ContatosSuporte, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_Geral_ContatosSuporte):
        ui_Geral_ContatosSuporte.setObjectName("ui_Geral_ContatosSuporte")
        ui_Geral_ContatosSuporte.resize(670, 631)
        ui_Geral_ContatosSuporte.setMinimumSize(QtCore.QSize(670, 631))
        ui_Geral_ContatosSuporte.setMaximumSize(QtCore.QSize(679, 642))
        self.verticalLayout_8 = QtGui.QVBoxLayout(ui_Geral_ContatosSuporte)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(ui_Geral_ContatosSuporte)
        self.textEdit.setMinimumSize(QtCore.QSize(661, 441))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_8.addWidget(self.textEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonFacebook = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonFacebook.setMinimumSize(QtCore.QSize(41, 36))
        self.pushButtonFacebook.setMaximumSize(QtCore.QSize(41, 36))
        self.pushButtonFacebook.setStyleSheet("background-image: url(:/Recursos/Imagens/facebook.png);")
        self.pushButtonFacebook.setText("")
        self.pushButtonFacebook.setObjectName("pushButtonFacebook")
        self.verticalLayout.addWidget(self.pushButtonFacebook)
        self.label_4 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonYoutube = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonYoutube.setMinimumSize(QtCore.QSize(41, 36))
        self.pushButtonYoutube.setMaximumSize(QtCore.QSize(41, 36))
        self.pushButtonYoutube.setStyleSheet("background-image: url(:/Recursos/Imagens/youtube.png);")
        self.pushButtonYoutube.setText("")
        self.pushButtonYoutube.setObjectName("pushButtonYoutube")
        self.verticalLayout_2.addWidget(self.pushButtonYoutube)
        self.label_5 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonTwitter = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonTwitter.setMinimumSize(QtCore.QSize(36, 36))
        self.pushButtonTwitter.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButtonTwitter.setStyleSheet("background-image: url(:/Recursos/Imagens/twitter.png);")
        self.pushButtonTwitter.setText("")
        self.pushButtonTwitter.setObjectName("pushButtonTwitter")
        self.verticalLayout_3.addWidget(self.pushButtonTwitter)
        self.label_6 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonMSDN = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonMSDN.setMinimumSize(QtCore.QSize(34, 36))
        self.pushButtonMSDN.setMaximumSize(QtCore.QSize(34, 36))
        self.pushButtonMSDN.setStyleSheet("background-image: url(:/Recursos/Imagens/msdn.png);")
        self.pushButtonMSDN.setText("")
        self.pushButtonMSDN.setObjectName("pushButtonMSDN")
        self.horizontalLayout_2.addWidget(self.pushButtonMSDN)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        spacerItem5 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButtonLinkedin = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonLinkedin.setMinimumSize(QtCore.QSize(36, 36))
        self.pushButtonLinkedin.setMaximumSize(QtCore.QSize(37, 36))
        self.pushButtonLinkedin.setStyleSheet("background-image: url(:/Recursos/Imagens/linkedin.png);")
        self.pushButtonLinkedin.setText("")
        self.pushButtonLinkedin.setObjectName("pushButtonLinkedin")
        self.verticalLayout_4.addWidget(self.pushButtonLinkedin)
        self.label_8 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButtonGoogle = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonGoogle.setMinimumSize(QtCore.QSize(38, 36))
        self.pushButtonGoogle.setMaximumSize(QtCore.QSize(38, 36))
        self.pushButtonGoogle.setStyleSheet("background-image: url(:/Recursos/Imagens/googleplus.png);")
        self.pushButtonGoogle.setText("")
        self.pushButtonGoogle.setObjectName("pushButtonGoogle")
        self.verticalLayout_5.addWidget(self.pushButtonGoogle)
        self.label_9 = QtGui.QLabel(ui_Geral_ContatosSuporte)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem7 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButtonFechar = QtGui.QPushButton(ui_Geral_ContatosSuporte)
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.verticalLayout_7.addWidget(self.pushButtonFechar)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(ui_Geral_ContatosSuporte)
        QtCore.QMetaObject.connectSlotsByName(ui_Geral_ContatosSuporte)

    def retranslateUi(self, ui_Geral_ContatosSuporte):
        ui_Geral_ContatosSuporte.setWindowTitle(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Contatos Suporte", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Contatos de Suporte ao Desenvolvedor -  Daruma Developers Community</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Telefone Gratuito:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span><span style=\" font-size:14pt; font-weight:600; color:#78bd2c;\">0800 770 3320</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">E-mails: (Exclusivo para o Suporte ao Desenvolvedor)</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial,sans-serif\'; font-size:12pt; color:#000000;\"></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" width=\"90%\" cellspacing=\"0\" cellpadding=\"0\">\n"
"<tr>\n"
"<td width=\"30%\" style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"><br /><br />Toda Linha de Impressoras Fiscais e não Fiscais e MicroTerminal (TA2000)</span><span style=\" font-size:8pt;\"> </span></p></td>\n"
"<td width=\"70%\" style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:suporte@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">suporte@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:desenvolvedores.suporte@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">desenvolvedores.suporte@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> </span><a href=\"mailto:desenvolvedores.daruma@daruma.com.br%20\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">desenvolvedores.daruma@daruma.com.br </span></a><a href=\"mailto:daruma.desenvolvedores@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">daruma.desenvolvedores@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:suporte.ddc@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">suporte.ddc@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"><br /></span><a href=\"mailto:ddc.suporte@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">ddc.suporte@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:suporte.desenvolvedores@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">suporte.desenvolvedores@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:suporte.alexandre@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">suporte.alexandre@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:claudenir@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">claudenir@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"><br />Toda a Linha de Thin Clients (MT1000)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:desenvolvedores.cpu@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">desenvolvedores.cpu@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:suporte.daruma@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">suporte.daruma@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\">Toda a Linha de Scanners, Kiosk e Modem</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:l.cavicchioli@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">desenvolvedores.kiosk@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:suporte.alexandre@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">suporte.alexandre@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> <br /></span><a href=\"mailto:claudenir@daruma.com.br\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; text-decoration: underline; color:#78bd2c;\">claudenir@daruma.com.br</span></a><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"> </span></p></td></tr></table>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#000000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#000000;\"><br /></span><span style=\" font-size:12pt; font-weight:600;\">Skype: (Exclusivo para o suporte ao Desenvolvedor)</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#000000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" width=\"90%\" cellspacing=\"0\" cellpadding=\"0\">\n"
"<tr>\n"
"<td width=\"30%\" style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\"><br /><br />Toda Linha de Impressoras Fiscais e não Fiscais e MicroTerminal (TA2000)</span><span style=\" font-size:8pt;\"> </span></p></td>\n"
"<td width=\"70%\" style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">suporte_daruma<br />desenvolvedores_suporte_daruma<br />suporte_desenvolvedores_daruma</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">desenvolvedores_daruma</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">daruma.desenvolvedores</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">suporte_ddc_daruma</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">ddc_suporte_daruma</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">daruma_suporte_alexandre</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">claudenir_andrade</span><span style=\" font-size:8pt; color:#78bd2c;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\">Toda a Linha de Thin Clients (MT1000)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\"><br />suporte.daruma</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">desenvolvedores_cpu_daruma</span><span style=\" font-size:8pt; color:#78bd2c;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#000000;\">Toda a Linha de Scanners, Kiosk e Modem</span><span style=\" font-size:8pt;\"> </span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">desenvolvedores_kiosk</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">daruma_suporte_alexandre</span><span style=\" font-size:8pt; color:#78bd2c;\"> <br /></span><span style=\" font-family:\'Arial,sans-serif\'; font-size:10pt; color:#78bd2c;\">claudenir_andrade</span><span style=\" font-size:8pt; color:#78bd2c;\"> </span></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Acompanhe a Daruma nas Redes Sociais!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Facebook", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Youtube", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Twitter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Fórum MSDN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Linkedin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Google+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_Geral_ContatosSuporte", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

