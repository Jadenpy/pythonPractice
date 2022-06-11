#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   qLabelBuddy.py    
@Contact :   huxinsheng2015@icloud.com
@License :   (C)Copyright 2017-2018

@Modify Time      @Author    @Version    
------------      -------    --------    -----------
2022/5/15 10:02   Jaden      1.0  

@Description :     
"""

from PyQt5.QtWidgets import *
import sys


# import PyQt5.QtWidgets.

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        buttonOK = QPushButton('&OK')
        buttonCancel = QPushButton('&Cancel')

        layoutUI = QGridLayout(self)

        layoutUI.addWidget(nameLabel, 0, 0)
        layoutUI.addWidget(nameLineEdit, 0, 1, 1, 2)

        layoutUI.addWidget(passwordLabel, 1, 0)
        layoutUI.addWidget(passwordLineEdit, 1, 1, 1, 2)

        layoutUI.addWidget(buttonOK, 2, 1)
        layoutUI.addWidget(buttonCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelBuddy()
    window.show()
    sys.exit(app.exec_())
