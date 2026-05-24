### THIS IS A TEMPLATE FILE, AND NOT A PLUGIN or a REAL WIDGET ! !   ! !!!!!!
### It is only for starting off a new plugin/widget and should be renamed and modified as needed!
### Add methods inside the specific widget's class for its use, and add buttons and UI elements if you need
### Make sure to change the PLUGIN Data at the very bottom of the file  for your new widget

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton
)
from PySide6.QtCore import Qt

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

        #layout.addWidget()

        layout.addStretch(1)
        self.setLayout(layout)
    
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    
# Plugin data
PLUGIN = {
    "name": "_Template",
    "keywords": ["template"],
    "widget": Template
}