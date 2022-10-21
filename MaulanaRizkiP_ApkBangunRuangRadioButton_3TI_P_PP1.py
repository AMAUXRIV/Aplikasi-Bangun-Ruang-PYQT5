import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDoubleValidator, QIntValidator

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.resize(400, 200)
        self.move(400, 300)
        self.setWindowTitle('Form Luas Volume')
        
        self.label1 = QLabel()
        self.label1.setText('Jari Jari')
        self.numberEdit1 = QLineEdit()
        self.numberEdit1.setValidator(QDoubleValidator(0.99,99.99,2))
        
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.numberEdit1)
        
        self.label2 = QLabel()
        self.label2.setText('Tinggi')
        self.numberEdit2 = QLineEdit()
        self.numberEdit2.setValidator(QDoubleValidator(0.99,99.99,2))
        
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.numberEdit2)

            #Radioedit
        
        self.radioedit=QRadioButton("Luas")
        
        self.radioedit2=QRadioButton("Volume")
        
        vboxrad= QHBoxLayout()
        vboxrad.addWidget(self.radioedit)
        vboxrad.addWidget(self.radioedit2)

       

        
    

        self.label3 = QLabel()
        self.label3.setText('Hasil        :')
        self.resultEdit = QLineEdit()
        self.resultEdit.setReadOnly(True)
        
        vbox3 = QHBoxLayout()
        vbox3.addWidget(self.label3)
        vbox3.addWidget(self.resultEdit)

        

        
        
        vbox4 = QVBoxLayout()
        vbox4.addLayout(vbox1)
        vbox4.addLayout(vbox2)
        vbox4.addLayout(vboxrad)
        vbox4.addLayout(vbox3)
        vbox4.addStretch()

        
        self.print = QPushButton('Print')
        
        vbox5 = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Maulana Rizki Pratama\n          21010026\n\n')
        vbox5.addWidget(self.label)
        vbox5.addStretch()
        vbox5.addWidget(self.print)
        vbox5.addStretch()
        
        layout  = QHBoxLayout()
        layout.addLayout(vbox4)
        verticalLine = QFrame();
        verticalLine.setFrameShape(QFrame.VLine)
        verticalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(verticalLine)
        layout.addLayout(vbox5)
        self.setLayout(layout)
        
        self.print.clicked.connect(self.btnstate)
        
        
    def calculate(self,operator):
        a = float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())
        if operator == 'ok':
            c = 2*3.14*a*(a+b)
            self.resultEdit.setText(str(c))
        elif operator == 'okk':
            c = 3.14*a*a*b
            self.resultEdit.setText(str(c))
       
        
        
    
        
    

    def btnstate(self):
        if self.radioedit.isChecked():
            self.calculate('ok')
        elif self.radioedit2.isChecked():
            self.calculate('okk')

        
        
if __name__=='__main__':
    a = QApplication(sys.argv)
    form=MainForm()
    form.show()
    a.exec_()
