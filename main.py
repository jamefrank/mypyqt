# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2023/08/29 23:52:35
@Author  :   frank 
@Version :   1.0
@Contact :   
@License :   
@Desc    :   None
"""

import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from Ui_cam2bev import Ui_Form


class Cam2BevWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Cam2BevWidget, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_file)

    def open_file(self):
        print("hello world")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Cam2BevWidget()
    widget.show()
    sys.exit(app.exec_())
