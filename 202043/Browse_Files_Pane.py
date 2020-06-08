# -*- coding: utf-8 -*-
from PyQt5.Qt import *
from resource.BrowseFiles_ui import Ui_Form
from resource.Function_Analyze import processing_data
from tkinter import *
import tkinter.filedialog
import os




class BrowseFile(QWidget, Ui_Form, processing_data):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("分析系统")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = BrowseFile()
    window.show()

    sys.exit(app.exec_())