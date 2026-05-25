'''
## CapyUtilities: Base64 Encoder/Decoder Widget
Description: Simple widget for encoding and decoding Base64. There are two sections for encoding and decoding.
Status: Stable
'''
import base64
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication  # Added for clipboard access
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
)


class Base64Widget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: Base64 Encoder/Decoder")
        self.go_home_callback = go_home_callback

        layout = QVBoxLayout()
        layout.setSpacing(10)

        # Back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # =ENCODER
        self.encode_label = QLabel("ENCODER")
        self.encode_label.setStyleSheet("font-weight: bold;")

        self.encode_input = QLineEdit()
        self.encode_input.setPlaceholderText("Enter Plaintext here...")

        # Output and Copy layout for Encoder
        encode_output_layout = QHBoxLayout()
        self.encode_output = QLabel("Encoded Base64 will appear here")
        self.encode_output.setWordWrap(True)
        
        self.copy_encode_btn = QPushButton("Copy")
        self.copy_encode_btn.setFixedWidth(60)
        self.copy_encode_btn.clicked.connect(self.copy_encoded_text)
        
        encode_output_layout.addWidget(self.encode_output, 1)  # Stretch factor 1 to take space
        encode_output_layout.addWidget(self.copy_encode_btn)

        self.encode_input.textChanged.connect(self.update_encode)

        layout.addWidget(self.encode_label)
        layout.addWidget(self.encode_input)
        layout.addLayout(encode_output_layout)

        layout.addSpacing(20)

        # DECODER
        self.decode_label = QLabel("DECODER")
        self.decode_label.setStyleSheet("font-weight: bold;")

        self.decode_input = QLineEdit()
        self.decode_input.setPlaceholderText("Enter Base64 string here...")

        # Output and Copy layout for Decoder
        decode_output_layout = QHBoxLayout()
        self.decode_output = QLabel("Decoded text will appear here")
        self.decode_output.setWordWrap(True)
        
        self.copy_decode_btn = QPushButton("Copy")
        self.copy_decode_btn.setFixedWidth(60)
        self.copy_decode_btn.clicked.connect(self.copy_decoded_text)
        
        decode_output_layout.addWidget(self.decode_output, 1)
        decode_output_layout.addWidget(self.copy_decode_btn)

        self.decode_input.textChanged.connect(self.update_decode)

        layout.addWidget(self.decode_label)
        layout.addWidget(self.decode_input)
        layout.addLayout(decode_output_layout)

        layout.addStretch(1)
        self.setLayout(layout)

    def update_encode(self):
        text = self.encode_input.text()
        if not text:
            self.encode_output.setText("Encoded Base64 will appear here")
            return
        encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        self.encode_output.setText(encoded)

    def update_decode(self):
        text = self.decode_input.text()
        if not text:
            self.decode_output.setText("Decoded text will appear here")
            return
        try:
            decoded = base64.b64decode(text.encode("utf-8")).decode("utf-8")
        except Exception:
            decoded = "Invalid Base64 input"
        self.decode_output.setText(decoded)

    def copy_encoded_text(self):
        text = self.encode_output.text()
        if text and text != "Encoded Base64 will appear here":
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

    def copy_decoded_text(self):
        text = self.decode_output.text()
        if text and text not in ["Decoded text will appear here", "Invalid Base64 input"]:
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

    # nav
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    def get_text(self, function):
        if function == "encode":
            return self.encode_input.text()
        if function == "decode":
            return self.decode_input.text()
        raise RuntimeError("Invalid function specified for get_text in Base64Widget!")


PLUGIN = {
    "name": "Base64 Encoder/Decoder",
    "keywords": ["base64", "base64 encoder", "base64 decoder", "base 64"],
    "widget": Base64Widget
}