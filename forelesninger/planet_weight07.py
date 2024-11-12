import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QFormLayout, QComboBox, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 11.15]


class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Planetvekt")
        self.setGeometry(100, 100, 500, 400)
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.topplabel = QLabel()
        self.topplabel.setText("Hva er din vekt på andre planeter?")
        self.layout.addWidget(self.topplabel, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.skjema = QFormLayout()
        self.meny_combobox = QComboBox()
        self.meny_combobox.setPlaceholderText("Velg en planet...")
        self.meny_combobox.addItem("Tilfeldig planet")
        for planet in planeter:
            self.meny_combobox.addItem(planet)
        self.meny_combobox.activated.connect(self.oppdater_bilde)
        self.skjema.addRow(self.meny_combobox)
        
        self.vekt_input = QDoubleSpinBox()
        self.vekt_input.setPrefix("Din vekt i kg:   ")
        self.vekt_input.setDecimals(1)
        self.skjema.addRow(self.vekt_input)
        
        self.regnutknapp = QPushButton("Regn ut")
        self.regnutknapp.clicked.connect(self.regn_ut)
        self.skjema.addRow(self.regnutknapp)
        
        self.layout.addLayout(self.skjema, 1, 0)
        
        self.bildelabel = QLabel()
        self.pixmap = QPixmap("forelesninger/bilder/sun.png")
        self.pixmap = self.pixmap.scaled(256, 256)
        self.bildelabel.setPixmap(self.pixmap)
        
        self.layout.addWidget(self.bildelabel, 1, 1)
        
        self.bunnlabel = QLabel("Velg en planet og skriv inn vekten din: ")
        self.layout.addWidget(self.bunnlabel, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.show()
        
    def oppdater_bilde(self, index):
        if index == 0:
            self.pixmap = QPixmap("forelesninger/bilder/sun.png")
        else:
            self.pixmap = QPixmap(f"forelesninger/bilder/{planeter[index-1].lower()}.png")
        self.pixmap = self.pixmap.scaled(256, 256)
        self.bildelabel.setPixmap(self.pixmap)
        
    def regn_ut(self):
        self.planetnummer = self.meny_combobox.currentIndex()
        
        if self.planetnummer == 0:
            self.planetnummer = random.randrange(1, len(planeter))
            self.ny_vekt = beregn_vekt(self.vekt_input.value(), tyngdekraft[self.planetnummer-1])
            self.bunnlabel.setText(f"Vekten din p  {planeter[self.planetnummer-1]} er {self.ny_vekt} kg.")
        
def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
    beregn_vekt = din_vekt / jordtyngdekraft * planettyngdekraft
    return round(beregn_vekt, 1)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())


