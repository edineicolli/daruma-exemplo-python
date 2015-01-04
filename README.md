DarumaFramework_Python_Qt
=====================

### Introdução

Exemplo Multiplataforma em Python utilizando a DarumaFramework.dll e DarumaFramework.so.

Os métodos foram reescritos em Python e a interface foi convertida do projeto original desenvolvido pela [Daruma](http://www.desenvolvedoresdaruma.com.br/home/index.php) em Qt C++.

### Conversão da interface com PySide

Comando para converter os arquivos .ui:
* pyside-uic -o output.py input.ui

Comando para converter o arquivo de recursos com as imagens para o Python igual ou superior a versão 3:
* pyside-rcc -py3 Recursos.qrc -o Recursos_rc.py

### Dependências

* [Python](https://www.python.org/) 3.4.2 ou superior
* [pydaruma](https://github.com/edineicolli/pydaruma) 0.1.9 ou superior
* [PySide](https://github.com/PySide) 1.2.2 ou superior
* [cx_Freeze](http://cx-freeze.sourceforge.net/) 4.3.3 ou superior
* DarumaFramework.dll 8.19.29.0 (Para Windows) ou libDarumaFramework.so (Para Linux)

cx_Freeze
http://www.lfd.uci.edu/~gohlke/pythonlibs/dpv9ch6y/cx_Freeze-4.3.3.win32-py3.4.exe<br>
http://www.lfd.uci.edu/~gohlke/pythonlibs/dpv9ch6y/cx_Freeze-4.3.3.win-amd64-py3.4.exe

### Instalação
```
git clone https://github.com/edineicolli/daruma-exemplo-python.git
cd daruma-exemplo-python
```
* Instalação - Windows
```
python main.py
```
* Instalação - Linux
```
sudo python3 main.py
```
### Build
```
git clone https://github.com/edineicolli/daruma-exemplo-python.git
cd daruma-exemplo-python
```
* Build - Windows
```
python setup.py build
```
* Build - Linux
```
sudo python3 setup.py build
```
### Feedback
Envie seu feedback para colli.edinei@gmail.com.