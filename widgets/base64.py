from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
)
from PySide6.QtCore import Qt

class Base64Widget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: Base64 Encoder/Decoder")

        self.go_home_callback = go_home_callback

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # A RANDOM JUMBLE OF UI ELEMENTS I WILL ORGANIZE later! :sob:
        self.encode_text = QLabel("ENCODER")
        
        self.encode_text.setStyleSheet("font-weight: bold;")
        self.decode_text = QLabel("DECODER")
        self.decode_text.setStyleSheet("font-weight: bold;")
        self.encode_output = QLabel("Encrypted Base64 Text will appear here")
        self.decode_output = QLabel("Decrypted Text will appear here")
        self.encode_output.setWordWrap(True)
        self.decode_output.setWordWrap(True)

        self.encode_input = QLineEdit()
        self.encode_input.setPlaceholderText("Enter Plaintext here...")
        self.decode_input = QLineEdit()
        self.decode_input.setPlaceholderText("Enter Base64 string here")

        ### ENCODER Ui
        layout.addWidget(self.encode_text) # the ENCODER label
        layout.addWidget(self.encode_input) # the input box for plaintext to be entered
        layout.addWidget(self.encode_output) # Where the encoded Base64 string will appear

        # add a space so it looks bettr
        layout.addSpacing(20)
        
        ### DECODER UI
        layout.addWidget(self.decode_text) # the decoder label
        layout.addWidget(self.decode_input) # the input box for base64 text to be entered
        layout.addWidget(self.decode_output)# Where the decoded plaintext will appear

        layout.addStretch(1)
        self.setLayout(layout)
    
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    def get_text(self, function):
        if function == "encode":
            return self.encode_input.text()
        if function == "decode":
            return self.decode_input.text()
        else:
            raise RuntimeError("Invalid function specified for get_text in Base64Widget!")

# Plugin data
PLUGIN = {
    "name": "Base64 Encoder/Decoder",
    "keywords": ["base64", "base64 encoder", "base64 decoder", "base 64"],
    "widget": Base64Widget
}