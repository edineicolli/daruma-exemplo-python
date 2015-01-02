# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_iimprimirtexto.ui'
#
# Created: Mon Nov 24 22:25:11 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
from ctypes import create_string_buffer

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iImprimirTexto_DUAL_DarumaFramework
from scripts.dual.retornodual import tratarRetornoDUAL


class Ui_ui_dual_iimprimirtexto(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_iimprimirtexto, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonTesteCompleto.clicked.connect(self.on_pushButtonTesteCompleto_clicked)
        self.pushButtonTesteSeparado.clicked.connect(self.on_pushButtonTesteSeparado_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)
        
    def on_pushButtonEnviar_clicked(self):
            StrTexto = self.TextEditTexto.toPlainText()

            tratarRetornoDUAL(iImprimirTexto_DUAL_DarumaFramework(StrTexto,0), self)
    
    def on_pushButtonTesteCompleto_clicked(self):
        iImprimirTexto_DUAL_DarumaFramework("<e><b>BUFFER COMPLETO</e></b><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e>DATA:<dt></dt></e><l></l><e>Hora:<hr></hr></e><l></l>",0)
        Texto = create_string_buffer(2000)
        Texto = ''.join([
            "<ce>Avançando 5 Linhas</ce><sl>5</sl>Inserindo<sp>10</sp>10 espaços em Branco<sl>2</sl>",
            "Formatação Normal</ce><l></l>DARUMA AUTOMAÇÃO!!<sl>2</sl><ce>Negr+Ital+Subl+Expand</ce><l></l>",
            "<b><i><s><e>DARUMA AUTOMAÇÃO!!</b></i></s></e><sl>2</sl><ce>Negr+Ital+Subl+Condensado</ce><l></l>",
            "<b><i><s><c>DARUMA AUTOMAÇÃO!!</b></i></s></c><sl>2</sl><ce>Negr+Ital+Subl+Normal</ce><l></l>",
            "<b><i><s><n>DARUMA AUTOMAÇÃO!!</b></i></s></n><sl>2</sl><ce>Expandido</ce><l></l>",
            "<e>DARUMA AUTOMAÇÃO!!</e><sl>2</sl><ce>Condensado</ce><l></l>",
            "<c>DARUMA AUTOMAÇÃO!!</c><sl>2</sl><ce>Negrito+Expandido</ce><l></l>",
            "<b><e>DARUMA AUTOMAÇÃO!!</b></e><sl>2</sl><ce>Itálico+Expandido</ce><l></l>",
            "<i><e>DARUMA AUTOMAÇÃO!!</i></e><sl>2</sl><ce>Sublinhado+Expandido</ce><l></l>",
            "<s><e>DARUMA AUTOMAÇÃO!!</s></e><sl>2</sl><ce>Negrito+Condensado</ce><l></l>",
            "<b><c>DARUMA AUTOMAÇÃO!!</b></c><sl>2</sl><ce>Itálico+Condensado</ce><l></l>",
            "<i><c>DARUMA AUTOMAÇÃO!!</i></c><sl>2</sl><ce>Sublinhado+Condensado</ce><l></l>",
            "<s><c>DARUMA AUTOMAÇÃO!!</s></c><sl>2</sl><ce>Negrito+Normal</ce><l></l>",
            "<b><n>DARUMA AUTOMAÇÃO!!</n></b><l></l>"
        ])
        iImprimirTexto_DUAL_DarumaFramework(Texto,0)
        iImprimirTexto_DUAL_DarumaFramework("<e><b>FIM BUFFER COMPLETO</b></e><sl>03</sl>", 0)
        iRetorno= iImprimirTexto_DUAL_DarumaFramework("<gui></gui>", 0)
        tratarRetornoDUAL(iRetorno, self)
    
    def on_pushButtonTesteSeparado_clicked(self):
        Texto = create_string_buffer(2000)
        iImprimirTexto_DUAL_DarumaFramework("<sn><l><ce><s>Teste com Formatação DHTM</s></ce>",0)
        Texto = ''.join([
            "<n>Estes são os carácteres que você poderá utilizar<n><l>Você poderá a qualquer monento combinar as formatações!!<l></l>",
            "<<i>><</i>> Para sinalizar Itálico<l></l>",
            "<<s>><</s>> Para sinalizar Sublinhado<l></l>",
            "<<e>><</e>> Para sinalizar Expandido<l></l>",
            "<<c>><</c>> Para sinalizar Condensado<l></l>",
            "<<n>><</n>> Para sinalizar Normal<l></l>",
            "<<l>><</l>> Para Saltar Uma Linha<l></l>",
            "<<fe>><</fe>> Ativa o Modo fonte Elite<l></l>",
            "<<b>><</b>> Para sinalizar Negrito<l></l>",
            "<<ad>><</ad>> Para alinhar a direita<l></l>",
            "<<ft>>n1,n2,...,n6<</ft>> Para habilitar tabulação<l></l>",
            "<<tb>><</tb>> Para saltar até a proxima tabulação<l></l>",
            "<<sl>>NN<</sl>> Para Saltar Várias Linhas<l></l>",
            "<<tc>>C<</tc>>Riscar Linha com Carácter Específico<l></l>",
            "<<ce>><</ce>> Para Centralizar<l></l>",
            "<<dt>><</dt>> Para Imprimir Data Atual<l></l>",
            "<<hr>><</hr>> Para Imprimir Hora Atual<l></l>",
            "<<sp>>NN<</sp>> Inserir NN Espaços em Branco<l></l>",
            "<<sn>><</sn>> Sinal Sonoro, Apitar<l></l>",
            "<<g>><</g>> Abre a Gaveta<l></l>",
            "<<a>><</a>> Aguardar até o Término da Impressão<l></l>",
            "<l><tc>_</tc><tc>_</tc><l></l>",
            "<e><ce>TABULAÇÃO</ce></e><l></l><tc>_</tc><l></l>",
            "<ft>05,10,15,20,30,40</ft><l></l>",
            "<tb>5</tb><tb>10</tb><tb>15</tb><tb>20</tb><tb>30</tb><tb>40</tb><l></l>",
            "<tb>5</tb><tb>10</tb><tb>15</tb><tb>20</tb><tb>30</tb><tb>40</tb><l></l>",
            "<tb>5</tb><tb>10</tb><tb>15</tb><tb>20</tb><tb>30</tb><tb>40</tb><l></l>",
            "<tb>5</tb><tb>10</tb><tb>15</tb><tb>20</tb><tb>30</tb><tb>40</tb><sl>02</sl>",
            "Data<tb></tb>Veiculo<tb></tb>Cor<tb></tb>Placa<tb></tb>Hora<l></l>",
            "<dt></dt><tb></tb>Golf<tb></tb><tb></tb>Branca<tb></tb>AJY5231<tb></tb>10:15<l></l>",
            "<dt></dt><tb></tb>Focus<tb></tb>Vermelha<tb></tb>APG2013<tb></tb>13:45<l></l>",
            "<dt></dt><tb></tb>Megane<tb></tb>Cinza<tb></tb>AAR5414<tb></tb>14:30<l></l>",
            "<dt></dt><tb></tb>Corsa<tb></tb>Preto<tb></tb>AWK0189<tb></tb>20:40<l></l>",
            "<l><tc>_</tc><l></l>",
            "<l></l><e>DATA:<dt></dt></e><l></l><e>Hora:<hr></hr></e><l></l><l></l>"
        ])
        iImprimirTexto_DUAL_DarumaFramework(Texto,0)
        iImprimirTexto_DUAL_DarumaFramework("<e><b>FIM BUFFER COMPLETO</b></e><sl>03</sl>", 0)
        iRetorno= iImprimirTexto_DUAL_DarumaFramework("<gui></gui>", 0)
        tratarRetornoDUAL(iRetorno, self)
    
    def on_pushButtonCancelar_clicked(self):
        self.close()

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

