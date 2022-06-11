#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   QLineEditValidator.py
@Contact :   huxinsheng2015@icloud.com
@License :   (C)Copyright 2017-2018

@Modify Time      @Author    @Version    
------------      -------    --------    -----------
2022/5/17 07:35   Jaden      1.0  

@Description :     
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框验证器')  # Widget窗口的标题

        formLayout = QFormLayout()  # 建立表单Layout

        intLineEdit = QLineEdit()  # 建立QLineEdit
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类形', intLineEdit)  # 将LineEdit控件加入到Layout
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('数字和字母', validatorLineEdit)

        intLineEdit.setPlaceholderText('整形')  # 设置Holder Text
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('数字&字母')

        # 建立校验器
        intValidator = QIntValidator()
        intValidator.setRange(1, 99)

        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator()
        validator.setRegExp(reg)

        # 绑定
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)  # 使widgets上的Layout生效


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditValidator()
    window.show()
    sys.exit(app.exec_())
