#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   QTextEditDemo.py    
@Contact :   huxinsheng2015@icloud.com
@License :   (C)Copyright 2017-2021

@Modify Time      @Author    @Version    
------------      -------    --------    
20/05/2022 16:18   Jaden Hu      1.0        

@Description：

"""

# import lib

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle('TextEdit演示')

        self.resize(300, 280)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText('不同按钮显示不一样的字体')
        # self.text_edit.alignment(Qt.Alignment)

        textButton = QPushButton('Text')
        htmlButton = QPushButton('Html')
        clearButton = QPushButton('Clear')

        verticalLayout = QVBoxLayout()

        verticalLayout.addWidget(self.text_edit)
        verticalLayout.addWidget(textButton)
        verticalLayout.addWidget(htmlButton)
        verticalLayout.addWidget(clearButton)

        textButton.clicked.connect(self.textButtonClick)
        htmlButton.clicked.connect(self.htmlButtonClick)
        clearButton.clicked.connect(self.clearButtonClick)

        self.setLayout(verticalLayout)

    def textButtonClick(self):
        self.text_edit.setPlainText('Hello ,Jaden.欢迎来到PyQt的世界')

    def htmlButtonClick(self):
        self.text_edit.setHtml('<font color="blue" size = "5">Hello ,Jaden.欢迎来到PyQt的世界</font>')

    def clearButtonClick(self):
        self.text_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTextEditDemo()
    window.show()
    sys.exit(app.exec_())
