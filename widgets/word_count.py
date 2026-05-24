from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
)
from PySide6.QtCore import Qt

class WordCountWidget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: Word Count")

        self.go_home_callback = go_home_callback

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Enter text here")
        self.output_label = QLabel("Number of characters will appear here")
        self.output_label.setWordWrap(True)
        layout.addWidget(self.output_label)

        layout.addWidget(self.input_text)

        layout.addStretch(1)
        self.setLayout(layout)
    
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    def get_text(self):
        return self.input_text.text()
    
    def return_char_count(self):
        text = self.get_text()
        char_count = len(text)
        self.output_label.setText(f"Character Count: {char_count}")
    
    

    
# Plugin data
PLUGIN = {
    "name": "Word Count Tool",
    "keywords": ["word count", "char count", "character", "count"],
    "widget": WordCountWidget
}