# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 393)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditOperator = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditOperator.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEditOperator.setStyleSheet("color: red")
        self.lineEditOperator.setObjectName("lineEditOperator")
        self.verticalLayout_2.addWidget(self.lineEditOperator)
        self.lineEditResult = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditResult.setObjectName("lineEditResult")
        self.verticalLayout_2.addWidget(self.lineEditResult)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtondivide = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtondivide.setObjectName("pushButtondivide")
        self.gridLayout_2.addWidget(self.pushButtondivide, 0, 3, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout_2.addWidget(self.pushButton8, 0, 1, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout_2.addWidget(self.pushButton9, 0, 2, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout_2.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout_2.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout_2.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButtonmultiple = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonmultiple.setObjectName("pushButtonmultiple")
        self.gridLayout_2.addWidget(self.pushButtonmultiple, 1, 3, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout_2.addWidget(self.pushButton7, 0, 0, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout_2.addWidget(self.pushButton1, 2, 0, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout_2.addWidget(self.pushButton3, 2, 2, 1, 1)
        self.pushButtonsubstract = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonsubstract.setObjectName("pushButtonsubstract")
        self.gridLayout_2.addWidget(self.pushButtonsubstract, 2, 3, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout_2.addWidget(self.pushButton2, 2, 1, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout_2.addWidget(self.pushButton0, 3, 0, 1, 1)
        self.pushButtondot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtondot.setObjectName("pushButtondot")
        self.gridLayout_2.addWidget(self.pushButtondot, 3, 1, 1, 1)
        self.pushButtonequal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonequal.setObjectName("pushButtonequal")
        self.gridLayout_2.addWidget(self.pushButtonequal, 3, 2, 1, 1)
        self.pushButtonad = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonad.setObjectName("pushButtonad")
        self.gridLayout_2.addWidget(self.pushButtonad, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.pushButtonNewOperation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonNewOperation.setObjectName("pushButtonNewOperation")
        self.verticalLayout_3.addWidget(self.pushButtonNewOperation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtondivide.setText(_translate("MainWindow", "/"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButtonmultiple.setText(_translate("MainWindow", "*"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButtonsubstract.setText(_translate("MainWindow", "-"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButtondot.setText(_translate("MainWindow", "."))
        self.pushButtonequal.setText(_translate("MainWindow", "="))
        self.pushButtonad.setText(_translate("MainWindow", "+"))
        self.pushButtonNewOperation.setText(_translate("MainWindow", "New Operation"))
