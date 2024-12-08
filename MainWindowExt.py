from MainWindow import Ui_MainWindow
class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButton0.clicked.connect(self.dis0)
        self.pushButton1.clicked.connect(self.dis1)
        self.pushButton2.clicked.connect(self.dis2)
        self.pushButton3.clicked.connect(self.dis3)
        self.pushButton4.clicked.connect(self.dis4)
        self.pushButton5.clicked.connect(self.dis5)
        self.pushButton6.clicked.connect(self.dis6)
        self.pushButton7.clicked.connect(self.dis7)
        self.pushButton8.clicked.connect(self.dis8)
        self.pushButton9.clicked.connect(self.dis9)
        self.pushButtonad.clicked.connect(self.disadd)
        self.pushButtondot.clicked.connect(self.disdot)
        self.pushButtondivide.clicked.connect(self.disdivide)
        self.pushButtonsubstract.clicked.connect(self.dissubstract)
        self.pushButtonmultiple.clicked.connect(self.dismultiple)
        self.pushButtonequal.clicked.connect(self.calculator)
        self.pushButtonNewOperation.clicked.connect(self.refresh)
    def refresh(self):
        self.lineEditResult.setText("")
    def calculator(self):
        expression = self.lineEditOperator.text()
        result = eval(expression)
        self.lineEditResult.setText(str(result))
    def dis0(self):
        text = self.lineEditOperator.text()
        text += "0"
        self.lineEditOperator.setText(text)
    def dis1(self):
        text = self.lineEditOperator.text()
        text += "1"
        self.lineEditOperator.setText(text)
    def dis2(self):
        text = self.lineEditOperator.text()
        text += "2"
        self.lineEditOperator.setText(text)
    def dis3(self):
        text = self.lineEditOperator.text()
        text += "3"
        self.lineEditOperator.setText(text)
    def dis4(self):
        text = self.lineEditOperator.text()
        text += "4"
        self.lineEditOperator.setText(text)
    def dis5(self):
        text = self.lineEditOperator.text()
        text += "5"
        self.lineEditOperator.setText(text)
    def dis6(self):
        text = self.lineEditOperator.text()
        text += "6"
        self.lineEditOperator.setText(text)
    def dis7(self):
        text = self.lineEditOperator.text()
        text += "7"
        self.lineEditOperator.setText(text)
    def dis8(self):
        text = self.lineEditOperator.text()
        text += "8"
        self.lineEditOperator.setText(text)
    def dis9(self):
        text = self.lineEditOperator.text()
        text += "9"
        self.lineEditOperator.setText(text)
    def disadd(self):
        text = self.lineEditOperator.text()
        text += "+"
        self.lineEditOperator.setText(text)
    def dissubstract(self):
        text = self.lineEditOperator.text()
        text += "-"
        self.lineEditOperator.setText(text)
    def dismultiple(self):
        text = self.lineEditOperator.text()
        text += "x"
        self.lineEditOperator.setText(text)
    def disdivide(self):
        text = self.lineEditOperator.text()
        text += "/"
        self.lineEditOperator.setText(text)
    def disdot(self):
        text = self.lineEditOperator.text()
        text += "."
        self.lineEditOperator.setText(text)
    def show(self):
        self.MainWindow.show()