'''
## CapyUtilities: CapyConvertWidget
Description: The home page of the suite of CapyConvert image utilities.
Status: Experimental
'''

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication  # Added for clipboard

class CapyConvertWidget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: CapyConvert")

        self.go_home_callback = go_home_callback

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.output_label = QLabel("Welcome to CapyConvert")
        self.output_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.output_label.setWordWrap(True)
        layout.addWidget(self.output_label)
        self.setLayout(layout)
        layout.addStretch(1)  # Pushes everything to the top
    
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()
    
    def copy_output(self):
        text = self.output_label.text()
        if text and text != "Formatted text will appear here":
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

