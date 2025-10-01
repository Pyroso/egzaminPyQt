import sys

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.colorButton.clicked.connect(self.getColor)
        self.ui.sliderRed.valueChanged.connect(self.updateColor)
        self.ui.sliderGreen.valueChanged.connect(self.updateColor)
        self.ui.sliderBlue.valueChanged.connect(self.updateColor)
        self.show()

    def updateColor(self):
        r = self.ui.sliderRed.value()
        g = self.ui.sliderGreen.value()
        b = self.ui.sliderBlue.value()

        self.ui.labelRed.setText(f"{r}")
        self.ui.labelGreen.setText(f"{g}")
        self.ui.labelBlue.setText(f"{b}")

        color = QColor(r, g, b)
        self.ui.colorEdit.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def getColor(self):
        r = self.ui.sliderRed.value()
        g = self.ui.sliderGreen.value()
        b = self.ui.sliderBlue.value()

        self.ui.labelColor.setText(f"{r}, {g}, {b}")
        self.ui.labelColor.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())