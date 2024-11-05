import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Hovedvindu(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setGeometry(200, 200, 300, 100)
        
        self.setWindowTitle("QVBoxLayout-test")
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = QPushButton('Knapp 1')
        button2 = QPushButton('Knapp 2')
        button3 = QPushButton('Knapp 3')
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addStretch()
        
        layout.setSpacing(20)
        layout.setContentsMargins(70, 70, 70, 70)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    
    sys.exit(app.exec())
