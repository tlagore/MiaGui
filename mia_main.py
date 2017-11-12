from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, 
    QMainWindow, QWidget, QMessageBox, QDesktopWidget, QAction, 
    qApp, QMenu, QTextEdit, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
import sys

class MiaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        """ set up ui """
        #set size
        self.resize(500, 500)

        #find and set center
        center = QDesktopWidget().availableGeometry().center()
        self.frameGeometry().moveCenter(center)

        #title
        self.setWindowTitle("Mama Mia!")

        #status shows at bottom of screen
        self.statusBar().showMessage('Ready')
        self.statusBar()

        #############################
        ####MENU BAR SET UP BEGIN####
        #############################
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(self.confirmClose)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        #doesnt work
        #fileMenu.addSeparator()
        
        #settings menu item
        settingsMenu = QMenu('Settings', self)
        fileMenu.addMenu(settingsMenu)

        #config submenu item of settingsMenu
        changeConfig = QAction('Change Config File', self)
        settingsMenu.addAction(changeConfig)


        fileMenu.addAction(exitAct)
        ##############################
        #### MENU BAR SET UP END #####
        ##############################

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        mainWidget = QWidget(self)
        self.setCentralWidget(mainWidget)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        mainWidget.setLayout(vbox)

        '''
        # if desired, adds a toolbar with an exit icon
        exitIcon = QAction(QIcon('exit.png'), 'Exit', self)
        exitIcon.triggered.connect(self.confirmClose)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitIcon)
        '''

        self.show()

    def confirmClose(self):
        reply = QMessageBox.question(self, 'Confirm',
            "Are you sure you want to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            qApp.quit()

    def closeEvent(self, event):
        """ handle close event - user trying to exit """
        reply = QMessageBox.question(self, 'Confirm',
            "Are you sure you want to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MiaApp()
    sys.exit(app.exec_())