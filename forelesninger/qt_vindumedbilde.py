import sys
from urllib.request import urlopen

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap


class Vindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enkelt vindu")
        self.resize(300, 300)

        label1 = QLabel()
        label1.setText("Hello World!")

        label_img = QLabel()
        pixmap = QPixmap()
        pixmap.load('bilde.jpg')
        pixmap = pixmap.scaled(200, 200)
        label_img.setPixmap(pixmap)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label1)
        layout.addWidget(label_img)


app = QApplication(sys.argv)
vindu = Vindu()
vindu.show()

sys.exit(app.exec())

