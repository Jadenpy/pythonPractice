#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   QLineEditEchoMode.py    
@Contact :   huxinsheng2015@icloud.com
@License :   (C)Copyright 2017-2018

@Modify Time      @Author    @Version    
------------      -------    --------    -----------
2022/5/17 07:35   Jaden      1.0  

@Description :     
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')  # Widget窗口的标题
        self.resize(400, 100)
        self.setWindowIcon(QIcon('kautex_Logo.bmp'))

        formLayout = QFormLayout()  # 建立表单Layout

        normalLineEdit = QLineEdit()  # 建立四个QLineEdit
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('Normal', normalLineEdit)  # 将4个LineEdit控件加入到Layout
        formLayout.addRow('NoEcho', noEchoLineEdit)
        formLayout.addRow('Password', passwordLineEdit)
        formLayout.addRow('PasswordOnEdit', passwordEchoOnEditLineEdit)
        #         place holder text for lineEdit
        normalLineEdit.setPlaceholderText('Normal')  # 设置Holder Text
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('Password')
        passwordEchoOnEditLineEdit.setPlaceholderText('PasswordOnEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)  # 设置回显模式
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)  # 使widgets上的Layout生效


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditEchoMode()
    window.show()
    sys.exit(app.exec_())
