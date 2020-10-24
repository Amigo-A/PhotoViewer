from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.update_photo_list()
        self.index = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 841, 511))
        self.label.setText("")

        if len(self.photo_list) > 0:
            self.label.setPixmap(QtGui.QPixmap(self.photo_list[self.index]))
        else:
            self.label.setText('No photos in current directory')

        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 520, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(":hover {\n"
"    background-color: silver;\n"
"}\n"
":clicked {\n"
"    background-color: black;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.previous_photo)
        

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 520, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(":hover {\n"
"    background-color: silver;\n"
"}\n"
":clicked {\n"
"    background-color: black;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect( self.next_photo )

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Super Good Photo Viewer"))
        self.pushButton.setText(_translate("MainWindow", "Previous"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))

    
    def next_photo(self):
        self.update_photo_list()
        self.index += 1
        if self.index > self.index_limit:
            self.index = 0
        self.label.setPixmap(QtGui.QPixmap(self.photo_list[self.index]))

    def previous_photo(self):
        self.update_photo_list()
        self.index -= 1
        if self.index < 0:
            self.index = self.index_limit
        self.label.setPixmap(QtGui.QPixmap(self.photo_list[self.index]))
        
    def update_photo_list(self):
        self.photo_list = []
        for file in os.listdir():
            if file.endswith('.png') or file.endswith('.jpg'):
                self.photo_list.append(file)
    
        len_list = len(self.photo_list)
        self.index_limit = len_list - 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
