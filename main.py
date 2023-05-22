from PyQt5 import  QtWidgets
import sys
import control
#from control import *
import torch.nn as nn
import torch
#import video_processing 
import os

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = control.MiApp()
    mi_app.show()
    sys.exit(app.exec_())

