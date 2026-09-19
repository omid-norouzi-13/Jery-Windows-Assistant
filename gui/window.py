import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QInputDialog
)

from core.assistant import JeryAssistant


class JeryWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.jery = JeryAssistant()

        self.setWindowTitle("Jery Assistant")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.title = QLabel("🤖 Jery")

        self.status = QLabel("Status: Ready")

        self.response = QLabel("")

        self.button = QPushButton("🎤 Listen")

        self.button.clicked.connect(self.listen)

        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.response)
        layout.addWidget(self.button)

        self.setLayout(layout)


    def listen(self):

        command, ok = QInputDialog.getText(
            self,
            "Jery Listening",
            "Command:"
        )

        if ok and command:

            result = self.jery.process_command(command)

            self.response.setText(
                "Jery: " + result
            )


app = QApplication(sys.argv)

window = JeryWindow()
window.show()

sys.exit(app.exec())