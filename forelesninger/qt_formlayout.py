import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton
class Hovedvindu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Oppmeldingsskjema")
        self.setGeometry(100, 100, 300, 100)
        
        layout = QFormLayout()    
        self.setLayout(layout)
        layout.addRow("Navn: ", QLineEdit(self))
        layout.addRow("E-post: ", QLineEdit(self))
        layout.addRow("Passord: ", QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow("Gjenta passordet: ", QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow(QPushButton("Meld meg opp"))
        
        
        
        self.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    vindu = Hovedvindu()
    sys.exit(app.exec())

