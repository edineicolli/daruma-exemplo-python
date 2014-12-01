daruma-exemplo-python
=====================

Exemplo Multiplataforma em Python usando a DarumaFramework.dll e DarumaFramework.so

A interface foi convertida do projeto em Qt utilizando pyside.

Comando para converter os arquivos .ui:<br>
pyside-uic -o output.py input.ui

Comando para converter o arquivo de recursos com as imagens para o python igual ou superior a versão 3:<br>
pyside-rcc -py3 Recursos.qrc -o Recursos_rc.py

cx_Freeze:
http://www.lfd.uci.edu/~gohlke/pythonlibs/dpv9ch6y/cx_Freeze-4.3.3.win32-py3.4.exe
http://www.lfd.uci.edu/~gohlke/pythonlibs/dpv9ch6y/cx_Freeze-4.3.3.win-amd64-py3.4.exe