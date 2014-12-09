# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowmodem.ui'
#
# Created: Mon Nov 24 22:25:08 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import eDefinirProduto_Daruma, eReiniciar_MODEM_DarumaFramework, \
    eInicializar_MODEM_DarumaFramework, eTrocarBandeja_MODEM_DarumaFramework, \
    eBuscarPortaVelocidade_MODEM_DarumaFramework, rListarSms_MODEM_DarumaFramework, \
    rNivelSinalRecebido_MODEM_DarumaFramework, regLerApagar_MODEM_DarumaFramework, regThread_MODEM_DarumaFramework
from scripts.modem.retornomodem import tratarRetornoModem, tratarRetornoModemReg
from scripts.modem.ui_modem_conexaocsd import Ui_ui_MODEM_ConexaoCSD
from scripts.modem.ui_modem_eapagar import Ui_ui_MODEM_eApagar
from scripts.modem.ui_modem_regbandejainicio import Ui_ui_MODEM_regBandejaInicio
from scripts.modem.ui_modem_regcaptionwinapp import Ui_ui_MODEM_regCaptionWinAPP
from scripts.modem.ui_modem_regporta import Ui_ui_MODEM_regPorta
from scripts.modem.ui_modem_regretornavalorchave import Ui_ui_MODEM_regRetornaValorChave
from scripts.modem.ui_modem_regtempoalertar import Ui_ui_MODEM_regTempoAlertar
from scripts.modem.ui_modem_regvelocidade import Ui_ui_MODEM_regVelocidade
from scripts.modem.ui_modem_rrecebersms import Ui_ui_MODEM_rReceberSms
from scripts.modem.ui_modem_rrecebersmsindice import Ui_ui_MODEM_rReceberSmsIndice
from scripts.modem.ui_modem_rretornarimei import Ui_ui_MODEM_rRetornarIMEI
from scripts.modem.ui_modem_rretornaroperadora import Ui_ui_MODEM_rRetornarOperadora
from scripts.modem.ui_modem_tenviarsms import Ui_ui_modem_tenviarsms
from scripts.modem.ui_modem_tenviarsmsoperadora import Ui_ui_MODEM_tEnviarSmsOperadora


class Ui_MainWindowModem(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindowModem, self).__init__()

        self.setupUi(self)

        self.pushButtonEncerrar.clicked.connect(self.on_pushButtonEncerrar_clicked)
        self.actionMetodo_eDefinirProduto_Daruma.triggered.connect(self.on_eDefinirProduto_Daruma_triggered)
        self.actionMetodo_tEnviarSms_MODEM_Daruma.triggered.connect(self.on_tEnviarSms_MODEM_Daruma_triggered)
        self.actionMetodo_regRetornaValorChave_DarumaFramework.triggered.connect(self.on_regRetornaValorChave_DarumaFramework_triggered)
        self.actionMetodo_regTempoAlertar_MODEM_DarumaFramework.triggered.connect(self.on_regTempoAlertar_MODEM_DarumaFramework_triggered)
        self.actionMetodo_regRetornaValorChave_DarumaFramework_2.triggered.connect(self.on_regRetornaValorChave_DarumaFramework_2_triggered)
        self.actionMetodo_regPorta_MODEM_DarumaFramework.triggered.connect(self.on_regPorta_MODEM_DarumaFramework_triggered)
        self.actionMetodo_regVelocidade_MODEM_DarumaFramework.triggered.connect(self.on_regVelocidade_MODEM_DarumaFramework_triggered)
        self.actionMetodo_regCaptionWinAPP_MODEM_DarumaFramework.triggered.connect(self.on_regCaptionWinAPP_MODEM_DarumaFramework_triggered)
        self.actionMetodo_regBandejaInicio_MODEM_DarumaFramework.triggered.connect(self.on_regBandejaInicio_MODEM_DarumaFramework_triggered)
        self.actionMetodo_eReiniciar_MODEM_DarumaFramework.triggered.connect(self.on_eReiniciar_MODEM_DarumaFramework_triggered)
        self.actionMetodo_eApagarSms_MODEM_DarumaFramework.triggered.connect(self.on_eApagarSms_MODEM_DarumaFramework_triggered)
        self.actionMetodo_eInicializar_MODEM_DarumaFramework.triggered.connect(self.on_eInicializar_MODEM_DarumaFramework_triggered)
        self.actionMetodo_eTrocarBandeja_MODEM_DarumaFramework.triggered.connect(self.on_eTrocarBandeja_MODEM_DarumaFramework_triggered)
        self.actionMetodo_eBuscarPortaVelocidade_MODEM_DarumaFramework.triggered.connect(self.on_eBuscarPortaVelocidade_MODEM_DarumaFramework_triggered)
        self.actionMetodo_tEnviarSmsOperadora_MODEM_Daruma.triggered.connect(self.on_tEnviarSmsOperadora_MODEM_Daruma_triggered)
        self.actionMetodo_rReceberSms_MODEM_DarumaFramework.triggered.connect(self.on_rReceberSms_MODEM_DarumaFramework_triggered)
        self.actionMetodo_rReceberSmsIndice_MODEM_DarumaFramework.triggered.connect(self.on_rReceberSmsIndice_MODEM_DarumaFramework_triggered)
        self.actionMetodo_rListarSms_MODEM_DarumaFramework.triggered.connect(self.on_rListarSms_MODEM_DarumaFramework_triggered)
        self.actionMetodo_rRetornarImei_MODEM_DarumaFramework.triggered.connect(self.on_rRetornarImei_MODEM_DarumaFramework_triggered)
        self.actionMetodo_rNivelSinalRecebido_MODEM_DarumaFramework.triggered.connect(self.on_rNivelSinalRecebido_MODEM_DarumaFramework_triggered)
        self.actionMetodo_rRetornarOperadora_MODEM_DarumaFramework.triggered.connect(self.on_rRetornarOperadora_MODEM_DarumaFramework_triggered)
        self.actionServi_o_CSD_DarumaFramework.triggered.connect(self.on_Servi_o_CSD_DarumaFramework_triggered)
        self.actionTRUELerApagar.triggered.connect(self.on_TRUELerApagar_triggered)
        self.actionFALSELerApagar.triggered.connect(self.on_FALSELerApagar_triggered)
        self.actionTRUEThread.triggered.connect(self.on_TRUEThread_triggered)
        self.actionFALSEThread.triggered.connect(self.on_FALSEThread_triggered)

    def on_pushButtonEncerrar_clicked(self):
        self.close()

    def on_eDefinirProduto_Daruma_triggered(self):
        iRetorno = eDefinirProduto_Daruma("MODEM");
        if(iRetorno == 1):
            QMessageBox.information(self, "Método eDefinirProduto_Daruma","Produto definido com sucesso!")
        else:
            QMessageBox.information(self,"Método eDefinirProduto_Daruma","Erro na definição de produto!")

    def on_tEnviarSms_MODEM_Daruma_triggered(self):
        self.form_MODEM_tEnviarSms = Ui_ui_modem_tenviarsms()
        self.form_MODEM_tEnviarSms.show()

    def on_regRetornaValorChave_DarumaFramework_triggered(self):
        self.form_MODEM_regRetornaValorChave = Ui_ui_MODEM_regRetornaValorChave()
        self.form_MODEM_regRetornaValorChave.show()

    def on_regTempoAlertar_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_regTempoAlertar = Ui_ui_MODEM_regTempoAlertar()
        self.form_MODEM_regTempoAlertar.show()

    def on_regRetornaValorChave_DarumaFramework_2_triggered(self):
        self.form_MODEM_regRetornaValorChave = Ui_ui_MODEM_regRetornaValorChave()
        self.form_MODEM_regRetornaValorChave.show()

    def on_regPorta_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_regPorta = Ui_ui_MODEM_regPorta()
        self.form_MODEM_regPorta.show()

    def on_regVelocidade_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_regVelocidade = Ui_ui_MODEM_regVelocidade()
        self.form_MODEM_regVelocidade.show()

    def on_regCaptionWinAPP_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_regCaptionWinAPP = Ui_ui_MODEM_regCaptionWinAPP()
        self.form_MODEM_regCaptionWinAPP.show()

    def on_regBandejaInicio_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_regBandejaInicio = Ui_ui_MODEM_regBandejaInicio();
        self.form_MODEM_regBandejaInicio.show();

    def on_eReiniciar_MODEM_DarumaFramework_triggered(self):
        tratarRetornoModem(eReiniciar_MODEM_DarumaFramework(), self);

    def on_eApagarSms_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_eApagarSms = Ui_ui_MODEM_eApagar()
        self.form_MODEM_eApagarSms.show()

    def on_eInicializar_MODEM_DarumaFramework_triggered(self):
        tratarRetornoModem(eInicializar_MODEM_DarumaFramework(), self)

    def on_eTrocarBandeja_MODEM_DarumaFramework_triggered(self):
        tratarRetornoModem(eTrocarBandeja_MODEM_DarumaFramework(), self)

    def on_eBuscarPortaVelocidade_MODEM_DarumaFramework_triggered(self):
        tratarRetornoModem(eBuscarPortaVelocidade_MODEM_DarumaFramework(), self)

    def on_tEnviarSmsOperadora_MODEM_Daruma_triggered(self):
        self.form_MODEM_tEnviarSmsOperadora = Ui_ui_MODEM_tEnviarSmsOperadora()
        self.form_MODEM_tEnviarSmsOperadora.show()

    def on_rReceberSms_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_rReceberSms = Ui_ui_MODEM_rReceberSms()
        self.form_MODEM_rReceberSms.show()

    def on_rReceberSmsIndice_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_rReceberSmsIndice = Ui_ui_MODEM_rReceberSmsIndice()
        self.form_MODEM_rReceberSmsIndice.show()

    def on_rListarSms_MODEM_DarumaFramework_triggered(self):
        tratarRetornoModem(rListarSms_MODEM_DarumaFramework(), self)

    def on_rRetornarImei_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_rRetornarIMEI = Ui_ui_MODEM_rRetornarIMEI()
        self.form_MODEM_rRetornarIMEI.show()

    def on_rNivelSinalRecebido_MODEM_DarumaFramework_triggered(self):
        tratarRetornoModem(rNivelSinalRecebido_MODEM_DarumaFramework(), self)

    def on_rRetornarOperadora_MODEM_DarumaFramework_triggered(self):
        self.form_MODEM_rRetornarOperadora = Ui_ui_MODEM_rRetornarOperadora();
        self.form_MODEM_rRetornarOperadora.show();

    def on_Servi_o_CSD_DarumaFramework_triggered(self):
        self.form_MODEM_ConexaoCSD = Ui_ui_MODEM_ConexaoCSD()
        self.form_MODEM_ConexaoCSD.show()

    def on_TRUELerApagar_triggered(self):
        tratarRetornoModemReg(regLerApagar_MODEM_DarumaFramework("TRUE"), self);

    def on_FALSELerApagar_triggered(self):
        tratarRetornoModemReg(regLerApagar_MODEM_DarumaFramework("FALSE"), self)

    def on_TRUEThread_triggered(self):
        tratarRetornoModemReg(regThread_MODEM_DarumaFramework("TRUE"), self)

    def on_FALSEThread_triggered(self):
        tratarRetornoModemReg(regThread_MODEM_DarumaFramework("FALSE"), self)
        
    def setupUi(self, MainWindowModem):
        MainWindowModem.setObjectName("MainWindowModem")
        MainWindowModem.resize(1361, 643)
        self.centralwidget = QtGui.QWidget(MainWindowModem)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 383, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 132))
        font = QtGui.QFont()
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(693, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(693, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButtonContatos_2 = QtGui.QPushButton(self.frame_2)
        self.pushButtonContatos_2.setMinimumSize(QtCore.QSize(191, 101))
        self.pushButtonContatos_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonContatos_2.setStyleSheet("background-image: url(:/Recursos/Imagens/avatar.png);")
        self.pushButtonContatos_2.setText("")
        self.pushButtonContatos_2.setObjectName("pushButtonContatos_2")
        self.horizontalLayout_2.addWidget(self.pushButtonContatos_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtGui.QSpacerItem(1178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButtonEncerrar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEncerrar.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButtonEncerrar.setObjectName("pushButtonEncerrar")
        self.horizontalLayout_3.addWidget(self.pushButtonEncerrar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindowModem.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowModem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1361, 21))
        self.menubar.setObjectName("menubar")
        self.menuM_todos_para_DarumaFramework = QtGui.QMenu(self.menubar)
        self.menuM_todos_para_DarumaFramework.setObjectName("menuM_todos_para_DarumaFramework")
        self.menuMetodos_para_Registro = QtGui.QMenu(self.menubar)
        self.menuMetodos_para_Registro.setObjectName("menuMetodos_para_Registro")
        self.menuM_todo_regLerApagar_MODEM_DarumaFramework = QtGui.QMenu(self.menuMetodos_para_Registro)
        self.menuM_todo_regLerApagar_MODEM_DarumaFramework.setObjectName("menuM_todo_regLerApagar_MODEM_DarumaFramework")
        self.menuM_todo_regThread_MODEM_DarumaFramework = QtGui.QMenu(self.menuMetodos_para_Registro)
        self.menuM_todo_regThread_MODEM_DarumaFramework.setObjectName("menuM_todo_regThread_MODEM_DarumaFramework")
        self.menuMetodos_de_Funcoes_para_Modem = QtGui.QMenu(self.menubar)
        self.menuMetodos_de_Funcoes_para_Modem.setObjectName("menuMetodos_de_Funcoes_para_Modem")
        self.menuMetodos_de_Transmissao_para_Modem = QtGui.QMenu(self.menubar)
        self.menuMetodos_de_Transmissao_para_Modem.setObjectName("menuMetodos_de_Transmissao_para_Modem")
        self.menuM_todos_de_Recep_o_para_Modem = QtGui.QMenu(self.menubar)
        self.menuM_todos_de_Recep_o_para_Modem.setObjectName("menuM_todos_de_Recep_o_para_Modem")
        self.menuServi_o_CSD_DarumaFramework = QtGui.QMenu(self.menubar)
        self.menuServi_o_CSD_DarumaFramework.setObjectName("menuServi_o_CSD_DarumaFramework")
        MainWindowModem.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowModem)
        self.statusbar.setObjectName("statusbar")
        MainWindowModem.setStatusBar(self.statusbar)
        self.actionMetodo_eDefinirProduto_Daruma = QtGui.QAction(MainWindowModem)
        self.actionMetodo_eDefinirProduto_Daruma.setObjectName("actionMetodo_eDefinirProduto_Daruma")
        self.actionMetodo_tEnviarSms_MODEM_Daruma = QtGui.QAction(MainWindowModem)
        self.actionMetodo_tEnviarSms_MODEM_Daruma.setObjectName("actionMetodo_tEnviarSms_MODEM_Daruma")
        self.actionMetodo_regRetornaValorChave_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regRetornaValorChave_DarumaFramework.setObjectName("actionMetodo_regRetornaValorChave_DarumaFramework")
        self.actionMetodo_regTempoAlertar_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regTempoAlertar_MODEM_DarumaFramework.setObjectName("actionMetodo_regTempoAlertar_MODEM_DarumaFramework")
        self.actionMetodo_regRetornaValorChave_DarumaFramework_2 = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regRetornaValorChave_DarumaFramework_2.setObjectName("actionMetodo_regRetornaValorChave_DarumaFramework_2")
        self.actionMetodo_regPorta_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regPorta_MODEM_DarumaFramework.setObjectName("actionMetodo_regPorta_MODEM_DarumaFramework")
        self.actionMetodo_regVelocidade_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regVelocidade_MODEM_DarumaFramework.setObjectName("actionMetodo_regVelocidade_MODEM_DarumaFramework")
        self.actionMetodo_regCaptionWinAPP_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regCaptionWinAPP_MODEM_DarumaFramework.setObjectName("actionMetodo_regCaptionWinAPP_MODEM_DarumaFramework")
        self.actionMetodo_regBandejaInicio_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_regBandejaInicio_MODEM_DarumaFramework.setObjectName("actionMetodo_regBandejaInicio_MODEM_DarumaFramework")
        self.actionMetodo_eReiniciar_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_eReiniciar_MODEM_DarumaFramework.setObjectName("actionMetodo_eReiniciar_MODEM_DarumaFramework")
        self.actionMetodo_eApagarSms_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_eApagarSms_MODEM_DarumaFramework.setObjectName("actionMetodo_eApagarSms_MODEM_DarumaFramework")
        self.actionMetodo_eInicializar_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_eInicializar_MODEM_DarumaFramework.setObjectName("actionMetodo_eInicializar_MODEM_DarumaFramework")
        self.actionMetodo_eTrocarBandeja_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_eTrocarBandeja_MODEM_DarumaFramework.setObjectName("actionMetodo_eTrocarBandeja_MODEM_DarumaFramework")
        self.actionMetodo_eBuscarPortaVelocidade_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_eBuscarPortaVelocidade_MODEM_DarumaFramework.setObjectName("actionMetodo_eBuscarPortaVelocidade_MODEM_DarumaFramework")
        self.actionMetodo_tEnviarSmsOperadora_MODEM_Daruma = QtGui.QAction(MainWindowModem)
        self.actionMetodo_tEnviarSmsOperadora_MODEM_Daruma.setObjectName("actionMetodo_tEnviarSmsOperadora_MODEM_Daruma")
        self.actionMetodo_rReceberSms_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_rReceberSms_MODEM_DarumaFramework.setObjectName("actionMetodo_rReceberSms_MODEM_DarumaFramework")
        self.actionMetodo_rReceberSmsIndice_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_rReceberSmsIndice_MODEM_DarumaFramework.setObjectName("actionMetodo_rReceberSmsIndice_MODEM_DarumaFramework")
        self.actionMetodo_rListarSms_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_rListarSms_MODEM_DarumaFramework.setObjectName("actionMetodo_rListarSms_MODEM_DarumaFramework")
        self.actionMetodo_rRetornarImei_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_rRetornarImei_MODEM_DarumaFramework.setObjectName("actionMetodo_rRetornarImei_MODEM_DarumaFramework")
        self.actionMetodo_rNivelSinalRecebido_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_rNivelSinalRecebido_MODEM_DarumaFramework.setObjectName("actionMetodo_rNivelSinalRecebido_MODEM_DarumaFramework")
        self.actionMetodo_rRetornarOperadora_MODEM_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionMetodo_rRetornarOperadora_MODEM_DarumaFramework.setObjectName("actionMetodo_rRetornarOperadora_MODEM_DarumaFramework")
        self.actionServi_o_CSD_DarumaFramework = QtGui.QAction(MainWindowModem)
        self.actionServi_o_CSD_DarumaFramework.setObjectName("actionServi_o_CSD_DarumaFramework")
        self.actionTRUELerApagar = QtGui.QAction(MainWindowModem)
        self.actionTRUELerApagar.setObjectName("actionTRUELerApagar")
        self.actionFALSELerApagar = QtGui.QAction(MainWindowModem)
        self.actionFALSELerApagar.setObjectName("actionFALSELerApagar")
        self.actionTRUEThread = QtGui.QAction(MainWindowModem)
        self.actionTRUEThread.setObjectName("actionTRUEThread")
        self.actionFALSEThread = QtGui.QAction(MainWindowModem)
        self.actionFALSEThread.setObjectName("actionFALSEThread")
        self.menuM_todos_para_DarumaFramework.addAction(self.actionMetodo_eDefinirProduto_Daruma)
        self.menuM_todos_para_DarumaFramework.addAction(self.actionMetodo_regRetornaValorChave_DarumaFramework_2)
        self.menuM_todo_regLerApagar_MODEM_DarumaFramework.addAction(self.actionTRUELerApagar)
        self.menuM_todo_regLerApagar_MODEM_DarumaFramework.addAction(self.actionFALSELerApagar)
        self.menuM_todo_regThread_MODEM_DarumaFramework.addAction(self.actionTRUEThread)
        self.menuM_todo_regThread_MODEM_DarumaFramework.addAction(self.actionFALSEThread)
        self.menuMetodos_para_Registro.addAction(self.actionMetodo_regTempoAlertar_MODEM_DarumaFramework)
        self.menuMetodos_para_Registro.addAction(self.menuM_todo_regLerApagar_MODEM_DarumaFramework.menuAction())
        self.menuMetodos_para_Registro.addAction(self.actionMetodo_regPorta_MODEM_DarumaFramework)
        self.menuMetodos_para_Registro.addAction(self.menuM_todo_regThread_MODEM_DarumaFramework.menuAction())
        self.menuMetodos_para_Registro.addAction(self.actionMetodo_regVelocidade_MODEM_DarumaFramework)
        self.menuMetodos_para_Registro.addAction(self.actionMetodo_regCaptionWinAPP_MODEM_DarumaFramework)
        self.menuMetodos_para_Registro.addAction(self.actionMetodo_regBandejaInicio_MODEM_DarumaFramework)
        self.menuMetodos_de_Funcoes_para_Modem.addAction(self.actionMetodo_eReiniciar_MODEM_DarumaFramework)
        self.menuMetodos_de_Funcoes_para_Modem.addAction(self.actionMetodo_eApagarSms_MODEM_DarumaFramework)
        self.menuMetodos_de_Funcoes_para_Modem.addAction(self.actionMetodo_eInicializar_MODEM_DarumaFramework)
        self.menuMetodos_de_Funcoes_para_Modem.addAction(self.actionMetodo_eTrocarBandeja_MODEM_DarumaFramework)
        self.menuMetodos_de_Funcoes_para_Modem.addAction(self.actionMetodo_eBuscarPortaVelocidade_MODEM_DarumaFramework)
        self.menuMetodos_de_Transmissao_para_Modem.addAction(self.actionMetodo_tEnviarSms_MODEM_Daruma)
        self.menuMetodos_de_Transmissao_para_Modem.addAction(self.actionMetodo_tEnviarSmsOperadora_MODEM_Daruma)
        self.menuM_todos_de_Recep_o_para_Modem.addAction(self.actionMetodo_rReceberSms_MODEM_DarumaFramework)
        self.menuM_todos_de_Recep_o_para_Modem.addAction(self.actionMetodo_rReceberSmsIndice_MODEM_DarumaFramework)
        self.menuM_todos_de_Recep_o_para_Modem.addAction(self.actionMetodo_rListarSms_MODEM_DarumaFramework)
        self.menuM_todos_de_Recep_o_para_Modem.addAction(self.actionMetodo_rRetornarImei_MODEM_DarumaFramework)
        self.menuM_todos_de_Recep_o_para_Modem.addAction(self.actionMetodo_rNivelSinalRecebido_MODEM_DarumaFramework)
        self.menuM_todos_de_Recep_o_para_Modem.addAction(self.actionMetodo_rRetornarOperadora_MODEM_DarumaFramework)
        self.menuServi_o_CSD_DarumaFramework.addAction(self.actionServi_o_CSD_DarumaFramework)
        self.menubar.addAction(self.menuM_todos_para_DarumaFramework.menuAction())
        self.menubar.addAction(self.menuMetodos_para_Registro.menuAction())
        self.menubar.addAction(self.menuMetodos_de_Funcoes_para_Modem.menuAction())
        self.menubar.addAction(self.menuMetodos_de_Transmissao_para_Modem.menuAction())
        self.menubar.addAction(self.menuM_todos_de_Recep_o_para_Modem.menuAction())
        self.menubar.addAction(self.menuServi_o_CSD_DarumaFramework.menuAction())

        self.retranslateUi(MainWindowModem)
        QtCore.QMetaObject.connectSlotsByName(MainWindowModem)

    def retranslateUi(self, MainWindowModem):
        MainWindowModem.setWindowTitle(QtGui.QApplication.translate("MainWindowModem", "DarumaFramework - Módulo MODEM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindowModem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Dúvidas? Ligue: 0800 77 0332 0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindowModem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Modem</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; font-weight:600;\">DLL: DarumaFramework.dll</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindowModem", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Recursos/Imagens/logo_daruma_developers.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEncerrar.setText(QtGui.QApplication.translate("MainWindowModem", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_para_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowModem", "Métodos para DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMetodos_para_Registro.setTitle(QtGui.QApplication.translate("MainWindowModem", "Métodos para Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regLerApagar_MODEM_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowModem", "Método regLerApagar_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regThread_MODEM_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowModem", "Método regThread_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMetodos_de_Funcoes_para_Modem.setTitle(QtGui.QApplication.translate("MainWindowModem", "Métodos de Funções para Modem", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMetodos_de_Transmissao_para_Modem.setTitle(QtGui.QApplication.translate("MainWindowModem", "Métodos de Transmissão para Modem", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_de_Recep_o_para_Modem.setTitle(QtGui.QApplication.translate("MainWindowModem", "Métodos de Recepção para Modem", None, QtGui.QApplication.UnicodeUTF8))
        self.menuServi_o_CSD_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowModem", "Conexão CSD", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_eDefinirProduto_Daruma.setText(QtGui.QApplication.translate("MainWindowModem", "Método eDefinirProduto_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_tEnviarSms_MODEM_Daruma.setText(QtGui.QApplication.translate("MainWindowModem", "Método tEnviarSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regRetornaValorChave_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regTempoAlertar_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método regTempoAlertar_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regRetornaValorChave_DarumaFramework_2.setText(QtGui.QApplication.translate("MainWindowModem", "Método regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regPorta_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método regPorta_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regVelocidade_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método regVelocidade_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regCaptionWinAPP_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método regCaptionWinAPP_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_regBandejaInicio_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método regBandejaInicio_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_eReiniciar_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método eReiniciar_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_eApagarSms_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método eApagarSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_eInicializar_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método eInicializar_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_eTrocarBandeja_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método eTrocarBandeja_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_eBuscarPortaVelocidade_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método eBuscarPortaVelocidade_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_tEnviarSmsOperadora_MODEM_Daruma.setText(QtGui.QApplication.translate("MainWindowModem", "Método tEnviarSmsOperadora_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_rReceberSms_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método rReceberSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_rReceberSmsIndice_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método rReceberSmsIndice_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_rListarSms_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método rListarSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_rRetornarImei_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método rRetornarImei_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_rNivelSinalRecebido_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método rNivelSinalRecebido_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMetodo_rRetornarOperadora_MODEM_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Método rRetornarOperadora_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionServi_o_CSD_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowModem", "Serviço CSD - DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTRUELerApagar.setText(QtGui.QApplication.translate("MainWindowModem", "TRUE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFALSELerApagar.setText(QtGui.QApplication.translate("MainWindowModem", "FALSE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTRUEThread.setText(QtGui.QApplication.translate("MainWindowModem", "TRUE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFALSEThread.setText(QtGui.QApplication.translate("MainWindowModem", "FALSE", None, QtGui.QApplication.UnicodeUTF8))

