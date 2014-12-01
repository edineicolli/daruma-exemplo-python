from scripts.widgetprincipal import Ui_WidgetPrincipal

__author__ = 'Edinei'

from PySide import QtGui

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Ui_WidgetPrincipal()
    window.show()
    sys.exit(app.exec_())
