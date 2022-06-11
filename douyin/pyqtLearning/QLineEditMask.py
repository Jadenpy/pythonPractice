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
import sys


class QLineEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mask模式')  # Widget窗口的标题

        formLayout = QFormLayout()  # 建立表单Layout

        ipLineEdit = QLineEdit()  # 建立QLineEdit
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('IP', ipLineEdit)  # 将LineEdit控件加入到Layout
        formLayout.addRow('MAC', macLineEdit)
        formLayout.addRow('Date', dateLineEdit)
        formLayout.addRow('License', licenseEchoOnEditLineEdit)
        # 设置掩码
        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setPlaceholderText('HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setPlaceholderText('0000-00-00;_')
        licenseEchoOnEditLineEdit.setPlaceholderText('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;*')

        self.setLayout(formLayout)  # 使widgets上的Layout生效


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditMask()
    window.show()
    sys.exit(app.exec_())
