# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mia_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.readwPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.readwPathTextBox.setGeometry(QtCore.QRect(20, 130, 301, 22))
        self.readwPathTextBox.setReadOnly(True)
        self.readwPathTextBox.setObjectName("readwPathTextBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 21))
        self.label_3.setObjectName("label_3")
        self.srcListView = QtWidgets.QListView(self.centralwidget)
        self.srcListView.setGeometry(QtCore.QRect(20, 200, 301, 101))
        self.srcListView.setObjectName("srcListView")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 141, 16))
        self.label_4.setObjectName("label_4")
        self.addSrcButton = QtWidgets.QPushButton(self.centralwidget)
        self.addSrcButton.setGeometry(QtCore.QRect(200, 310, 120, 30))
        self.addSrcButton.setObjectName("addSrcButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 160, 120, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.menuFile.addAction(self.actionMinimize)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mama Mia!"))
        self.label_2.setText(_translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "ReAdW path"))
        self.label_4.setText(_translate("MainWindow", "Source Dirrectories"))
        self.addSrcButton.setText(_translate("MainWindow", "Add Source"))
        self.pushButton.setText(_translate("MainWindow", "Choose Location"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Ui_MainWindow()
    sys.exit(app.exec_())