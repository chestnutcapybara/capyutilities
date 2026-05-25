'''
## CapyUtilities: QrCodeWidget
Description: Minimalist QR Code Generator
Status: Stable
'''

from io import BytesIO

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QPixmap

import qrcode


class QrCodeWidget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: QrCodeWidget")

        self.go_home_callback = go_home_callback
        self.current_pixmap = None

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # Back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)
        layout.addWidget(
            back_button,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        # Input box
        self.link_query = QTextEdit()
        self.link_query.setPlaceholderText("Enter the link...")
        self.link_query.setFixedHeight(80)

        # Generate button
        self.link_btn = QPushButton("Generate QR Code")
        self.link_btn.clicked.connect(
            lambda: self.generate_qr(self.link_query.toPlainText())
        )

        # QR output
        self.output_label = QLabel()
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_label.setMinimumHeight(100)

        # Copy button
        self.copy_output_btn = QPushButton("Copy QR")
        self.copy_output_btn.setFixedWidth(100)
        self.copy_output_btn.clicked.connect(self.copy_output)

        layout.addWidget(self.link_query)
        layout.addWidget(self.link_btn)
        layout.addWidget(self.output_label)
        layout.addWidget(self.copy_output_btn)

        layout.addStretch(1)
        self.setLayout(layout)

    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    def copy_output(self):
        if self.current_pixmap is not None:
            clipboard = QGuiApplication.clipboard()
            clipboard.setPixmap(self.current_pixmap)

    def generate_qr(self, link):
        link = link.strip()

        if not link:
            self.output_label.setText("Please enter a link or text.")
            return

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=2
        )

        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").get_image()

        # convert pillow img to Qt Pixmap without saving to disk.
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())

        self.current_pixmap = pixmap

        self.output_label.setPixmap(
            pixmap.scaled(
                100,
                100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )


# Plugin data
PLUGIN = {
    "name": "QR Code Generator",
    "keywords": ["qrcode", "qr code", "qr", "generator"],
    "widget": QrCodeWidget
}