import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Test av knappbinding")
        self.setGeometry(100, 100, 300, 100)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        knapp = QPushButton("Min knapp")
        knapp.clicked.connect(self.knapp_trykket)
        layout.addWidget(knapp)
        self.show()
        
        
    def knapp_trykket(self):
        print("Knappen ble trykket!")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
        
    vindu = Hovedvindu()
    sys.exit(app.exec())

