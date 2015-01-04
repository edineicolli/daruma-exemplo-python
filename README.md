DarumaFramework_Python_Qt
=====================

### Introdução

Exemplo Multiplataforma em Python utilizando a DarumaFramework.dll e libDarumaFramework.so.

Os métodos foram reescritos em Python e a interface foi convertida do projeto original desenvolvido pela [Daruma](http://www.desenvolvedoresdaruma.com.br/home/index.php) em Qt C++.

### Conversão da interface com PySide

Comando para converter os arquivos .ui:
```
> pyside-uic -o output.py input.ui
```
Comando para converter o arquivo de recursos com as imagens para o Python igual ou superior a versão 3:
```
> pyside-rcc -py3 Recursos.qrc -o Recursos_rc.py
```

### Dependências

* [Python](https://www.python.org/) 3.4.2 ou superior
* [pydaruma](https://github.com/edineicolli/pydaruma) 0.1.9 ou superior
* [PySide](https://github.com/PySide) 1.2.2 ou superior
* [cx_Freeze](http://cx-freeze.sourceforge.net/) 4.3.3 ou superior
* DarumaFramework.dll 8.19.29.0 (Para Windows) ou libDarumaFramework.so (Para Linux)

### Instalação

* Instalação - Windows

Copie a biblioteca DarumaFramework.dll para a mesma pasta do arquivo main.py
```
> git clone https://github.com/edineicolli/daruma-exemplo-python.git
> cd daruma-exemplo-python
> python main.py
```
* Instalação - Linux

```
$ mkdir /usr/local/sahre/DarumaFramework
$ chmod 777 DarumaFramework
# Copie a biblioteca libDarumaFramework.so para /usr/local/lib.
$ chmod 777 /usr/local/lib/libDarumaFramework.so
$ git clone https://github.com/edineicolli/daruma-exemplo-python.git
$ cd daruma-exemplo-python
$ python3 main.py
```

Basicamente os passos são os mesmos utilizados no exemplo original em Qt C++ desenvolvido pela Daruma, [veja aqui](http://www.daruma.com.br/ddemkt/dde023_2012.html).

### Build

Congele os script Python em arquivo binário utilizando cx_Freeze. 
* Build - Windows
```
> git clone https://github.com/edineicolli/daruma-exemplo-python.git
> cd daruma-exemplo-python
> python setup.py build
```

**Observação**: Para cx_Freeze em Windows, utilize os instaladores disponíveis em:
http://www.lfd.uci.edu/~gohlke/pythonlibs/dpv9ch6y/cx_Freeze-4.3.3.win32-py3.4.exe
http://www.lfd.uci.edu/~gohlke/pythonlibs/dpv9ch6y/cx_Freeze-4.3.3.win-amd64-py3.4.exe

* Build - Linux
```
$ git clone https://github.com/edineicolli/daruma-exemplo-python.git
$ cd daruma-exemplo-python
$ sudo python3 setup.py build
```
### Feedback
Envie seu feedback para colli.edinei@gmail.com.