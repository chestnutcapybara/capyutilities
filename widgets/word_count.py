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

        self.output_label = QLabel("Number of characters will appear here")
        self.output_label.setWordWrap(True)

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Enter text here")

        self.count_char = QPushButton("Count Characters")
        self.count_char.clicked.connect(self.return_char_count)

        self.count_char_nospaces = QPushButton("Count Characters (no spaces)")
        self.count_char_nospaces.clicked.connect(self.return_char_count_nospaces)

        self.word_count = QPushButton("Word Count")
        self.word_count.clicked.connect(self.return_word_count)

        layout.addWidget(self.input_text)
        layout.addWidget(self.count_char)
        layout.addWidget(self.count_char_nospaces)
        layout.addWidget(self.word_count)
        layout.addWidget(self.output_label)
        
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

    def return_char_count_nospaces(self):
        text = self.get_text()
        char_count = len(text.replace(" ", ""))
        self.output_label.setText(f"Character Count (no spaces): {char_count}")

    def return_word_count(self):
        text = self.get_text()
        word_count = len(text.split())
        self.output_label.setText(f"Word Count: {word_count}")

# Plugin data
PLUGIN = {
    "name": "Word Count Tool",
    "keywords": ["word count", "char count", "character", "count"],
    "widget": WordCountWidget
}