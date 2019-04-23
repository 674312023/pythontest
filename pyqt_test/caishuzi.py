# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caishuzi.ui'
#
# Created: Thu Dec  6 14:09:31 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from random import randint
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.lineEdit.setToolTip("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.showmessage_click)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.num=randint(1,100)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "猜数字游戏"))
        self.pushButton.setToolTip(_translate("Form", "<b>点击这里猜数字<b>"))
        self.pushButton.setText(_translate("Form", "猜数字"))
        self.lineEdit.setText(_translate("Form", "在这里猜数字"))
        self.pushButton_2.setToolTip(_translate("Form", "<b>点击这里猜数字<b>"))
        self.pushButton_2.setText(_translate("Form", "猜数字"))

