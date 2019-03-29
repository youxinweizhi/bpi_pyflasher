#!/usr/bin/env python
# coding: utf-8
'''
@File   :AutoErase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''
import control
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_Form
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.main)
        self.checkBox_3.stateChanged.connect(self.disable_op)
        self.setFixedSize(self.width(), self.height())#固定窗口大小
        self.setWindowIcon(QIcon('./image/icon.ico'))
        self.statusBar().showMessage(" by: youxinweizhi")
        self.get_com()
        self.get_bin()

    def disable_op(self):
        if self.checkBox_3.isChecked():
            self.comboBox_2.setDisabled(True)
            # self.comboBox.setDisabled(True)
            self.checkBox.setDisabled(True)
            self.checkBox_2.setDisabled(True)
        else:
            self.comboBox_2.setDisabled(False)
            # self.comboBox.setDisabled(False)
            self.checkBox.setDisabled(False)
            self.checkBox_2.setDisabled(False)
    def get_com(self):
        self.comboBox.addItems(control.list_serial())

    def get_bin(self):
        self.comboBox_2.addItems(control.list_bin())

    def erase_flash(self):
        self.statusBar().showMessage(control.flash_erase(self.com))
        self.flasher()

    def flasher(self):
        self.statusBar().showMessage('开始刷新固件...')
        self.statusBar().showMessage(control.flash_bin(self.checkBox_2.isChecked(), self.com, self.firmware))

    def adv_flasher(self):
        import advanced
        self.statusBar().showMessage(advanced.flash_bin(self.com))

    def adv(self):
        import advanced
        self.statusBar().showMessage(advanced.run(self.adv_flasher))

    def main(self):
        self.com = self.comboBox.currentText().split(" - ",1)[0]
        # print(self.com)
        self.firmware = self.comboBox_2.currentText()
        if self.checkBox_3.isChecked():
            self.adv()
        else:
            self.statusBar().showMessage(control.run(self.checkBox.isChecked(), self.erase_flash, self.flasher))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
