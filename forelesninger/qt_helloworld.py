import sys
from asyncio import wait_for

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

vindu = QWidget()

vindu.setWindowTitle("Hello World!")
vindu.resize(300, 100)
vindu.move(700, 300)

vindu.show()

sys.exit(app.exec())
