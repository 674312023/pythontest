# -*- coding: utf-8 -*-
import sys
# from PyQt5.QtWidgets import QApplication , QMainWindow
from pyqt_test.caishuzi import *
from PyQt5 import QtWidgets
class main(QtWidgets.QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)

    def showmessage_click(self):
        guessnumber=int(self.lineEdit.text())
        print(self.num)
        if guessnumber > self.num:
            QMessageBox.about(self, '看结果','猜大了!')
            self.lineEdit.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果','猜小了!')
            self.lineEdit.setFocus()
        else:
            QMessageBox.about(self, '看结果','答对了!进入下一轮!')
            self.num = randint(1,100)
            self.lineEdit.clear()
            self.lineEdit.setFocus()
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    myshow=main()
    myshow.show()
    sys.exit(app.exec_())