import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        # Grid Layout
        grid = QGridLayout()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '⌫'
        ]

        row = 0
        col = 0

        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.layout.addLayout(grid)
        self.setLayout(self.layout)

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")

        elif text == "C":   # Clear All
            self.display.clear()

        elif text == "⌫":   # Backspace (Cancel last digit)
            current = self.display.text()
            self.display.setText(current[:-1])

        else:
            self.display.setText(self.display.text() + text)


app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())