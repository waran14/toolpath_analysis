# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dinesh\PycharmProjects\learning\simple.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filename.setGeometry(QtCore.QRect(120, 20, 541, 31))
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(290, 60, 181, 31))
        self.label_status.setObjectName("label_status")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(680, 20, 93, 28))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(680, 60, 93, 28))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 100, 93, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 91, 20))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(230, 100, 46, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(230, 130, 46, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 220, 551, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_status.setText(_translate("MainWindow", "Waiting for file upload"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.label.setText(_translate("MainWindow", "Select File"))
        self.pushButton.setText(_translate("MainWindow", "Parse"))
        self.label_2.setText(_translate("MainWindow", "Starting Layer"))
        self.label_3.setText(_translate("MainWindow", "Ending Layer"))

