import sys

from PyQt6.QtWidgets import QApplication
from gui.window import JeryWindow


app = QApplication(sys.argv)

window = JeryWindow()

window.show()

sys.exit(app.exec())