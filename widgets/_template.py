### THIS IS A TEMPLATE FILE, AND NOT A PLUGIN or a REAL WIDGET ! !   ! !!!!!!
### It is only for starting off a new plugin/widget and should be renamed and modified as needed!
### Add methods inside the specific widget's class for its use, and add buttons and UI elements if you need
### Make sure to change the PLUGIN Data at the very bottom of the file  for your new widget

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication  # Added for clipboard

class Template(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: TEMPLATE")

        self.go_home_callback = go_home_callback

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.output_label = QLabel("This is a template")
        self.output_label.setWordWrap(True)
        self.copy_output_btn = QPushButton("Copy")
        self.copy_output_btn.setFixedWidth(60)
        self.copy_output_btn.clicked.connect(self.copy_output)
        output_layout = QHBoxLayout()

        output_layout.addWidget(self.output_label, 1)  # Stretch factor
        output_layout.addWidget(self.copy_output_btn)

        layout.addLayout(output_layout)
        

        layout.addStretch(1)
        self.setLayout(layout)
    
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()
    
    def copy_output(self):
        text = self.output_label.text()
        if text and text != "Formatted text will appear here":
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

    
# Plugin data
PLUGIN = {
    "name": "_Template",
    "keywords": ["template"],
    "widget": Template
}