#import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
#from PyQt5.QtGui import QColor
#from PyQt5 import QtCore, QtWidgets
#from PyQt5.uic import loadUi
import final_cctv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
import control

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = control.MiApp()
     mi_app.show()
     sys.exit(app.exec_())  


'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_cctv_2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
