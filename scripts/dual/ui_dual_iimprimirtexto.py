# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_iimprimirtexto.ui'
#
# Created: Mon Nov 24 22:25:11 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_iimprimirtexto(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_iimprimirtexto, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_dual_iimprimirtexto):
        ui_dual_iimprimirtexto.setObjectName("ui_dual_iimprimirtexto")
        ui_dual_iimprimirtexto.resize(679, 527)
        self.groupBox = QtGui.QGroupBox(ui_dual_iimprimirtexto)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 431))
        self.groupBox.setObjectName("groupBox")
        self.TextEditTexto = QtGui.QTextEdit(self.groupBox)
        self.TextEditTexto.setGeometry(QtCore.QRect(10, 20, 301, 401))
        self.TextEditTexto.setObjectName("TextEditTexto")
        self.groupBox_2 = QtGui.QGroupBox(ui_dual_iimprimirtexto)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 10, 331, 511))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 501))
        self.label.setObjectName("label")
        self.pushButtonTesteCompleto = QtGui.QPushButton(ui_dual_iimprimirtexto)
        self.pushButtonTesteCompleto.setGeometry(QtCore.QRect(10, 450, 151, 31))
        self.pushButtonTesteCompleto.setObjectName("pushButtonTesteCompleto")
        self.pushButtonTesteSeparado = QtGui.QPushButton(ui_dual_iimprimirtexto)
        self.pushButtonTesteSeparado.setGeometry(QtCore.QRect(180, 450, 151, 31))
        self.pushButtonTesteSeparado.setObjectName("pushButtonTesteSeparado")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_iimprimirtexto)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(180, 490, 151, 31))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_iimprimirtexto)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(10, 490, 151, 31))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")

        self.retranslateUi(ui_dual_iimprimirtexto)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_iimprimirtexto)

    def retranslateUi(self, ui_dual_iimprimirtexto):
        ui_dual_iimprimirtexto.setWindowTitle(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "Método iImprimirTexto_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "Digite o Texto:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "TAGS", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Centralizado: &lt;ce&gt;centralizado&lt;/ce&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Negrito: &lt;b&gt;negrito&lt;/b&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Itálico: &lt;i&gt;Itálico&lt;/i&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Sublinhado: &lt;s&gt;Sublinhado&lt;/s&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Expandido: &lt;e&gt;Expandido&lt;/e&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Condensado: &lt;c&gt;condensado&lt;/c&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto Normal: &lt;n&gt;Normal&lt;/n&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saltar uma Linha: &lt;l&gt;&lt;/l&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saltar várias Linhas: &lt;sl&gt;NN&lt;/sl&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Riscar linha com caráctere especifico: &lt;tc&gt;C&lt;/tc&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Imprimir data atual: &lt;dt&gt;&lt;/dt&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Imprimir hora atual: &lt;hr&gt;&lt;/hr&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Inserir espaços em branco: &lt;sp&gt;NN&lt;/sp&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sinal sonoro, apitar: &lt;sn&gt;&lt;/sn&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Abre gaveta de dinheiro: &lt;g&gt;&lt;/g&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aguardar o término da impressão: &lt;a&gt;&lt;/a&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tabulação: &lt;tb&gt;&lt;/tb&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alinhando a Direita: &lt;ad&gt;&lt;/ad&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Duplicar a altura do caractere: &lt;da&gt;&lt;/da&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Habilita o modo fonte elite: &lt;fe&gt;texto&lt;/fe&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Imprimindo Codigos de Barras:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;ean13&gt;123456789012&lt;/ean13&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;ean8&gt;1234567&lt;/ean8&gt;  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;upc-a&gt;12345678901&lt;/upc-a&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;code39&gt;CODE 39&lt;/code39&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;code93&gt;CODE 93&lt;/code93&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;codabar&gt;CODABAR&lt;/codabar&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;msi&gt;123456789&lt;/msi&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;code11&gt;12345678901&lt;/code11&gt; </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;pdf&gt;12345&lt;/pdf&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;code128&gt;&lt;txt&gt;123456789123-A-B-*_%-&amp;&lt;/txt&gt;&lt;/code128&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;i2of5&gt;&lt;cbv&gt;1234&lt;/cbv&gt;&lt;/i2of5&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;s2of5&gt;&lt;txt&gt;12345678&lt;/txt&gt;&lt;/s2of5&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Comandos:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Carregar logotipo: &lt;bmp&gt;&lt;/bmp&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Acionar guilhotina: &lt;gui&gt;&lt;/gui&gt;</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTesteCompleto.setText(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "Teste completo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTesteSeparado.setText(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "Teste completo (separado)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_iimprimirtexto", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

