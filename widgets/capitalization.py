'''
## CapyUtilities: CapitalizationWidget
Description: A simple widget for changing the capitalization of text. It has 3 options, 
    Uppercase, Lowercase, and Title Case.
Status: Stable
'''
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication  # Added for clipboard stufffs

class CapitalizationWidget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("Bingy Utilities: Capitalization Tool")

        self.go_home_callback = go_home_callback

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Input box
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text here...")
        self.input_text.setFixedHeight(30)

        #self.input_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Output label
        self.output_label = QLabel("Formatted text will appear here")
        self.output_label.setWordWrap(True)

        self.copy = QPushButton("Copy")
        self.copy.setFixedWidth(60)
        self.copy.clicked.connect(self.copy_output)
        
        # Buttons
        btn_upper = QPushButton("Uppercase (EXAMPLE)")
        btn_title = QPushButton("Title Case (Example)")
        btn_lower = QPushButton("Lowercase (example)" )

        # Connect buttons
        btn_upper.clicked.connect(self.to_upper)
        btn_title.clicked.connect(self.to_title) 
        btn_lower.clicked.connect(self.to_lower)

        # Add to layout
        layout.addWidget(self.input_text)
        layout.addWidget(btn_upper)
        layout.addWidget(btn_title)
        layout.addWidget(btn_lower)
        output_layout = QHBoxLayout()

        output_layout.addWidget(self.output_label, 1)  # Stretch factor
        output_layout.addWidget(self.copy)

        layout.addLayout(output_layout)

        layout.addStretch(1)
        self.setLayout(layout)
    
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    def get_text(self):
        return self.input_text.toPlainText()

    def to_upper(self):
        self.output_label.setText(self.get_text().upper())

    def to_title(self):
        self.output_label.setText(self.get_text().title())

    def to_lower(self):
        self.output_label.setText(self.get_text().lower())

    def copy_output(self):
        text = self.output_label.text()
        if text and text != "Formatted text will appear here":
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)


# Plugin data
PLUGIN = {
    "name": "Capitalization Tool",
    "keywords": ["caps", "uppercase", "lowercase", "title", "text"],
    "widget": CapitalizationWidget
}