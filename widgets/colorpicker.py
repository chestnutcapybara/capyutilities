'''
## CapyUtilities: ColorPickerWidget
Description: A simple color picker widget, consisting of both RGB and HEX and can be used to convert between the two
Status: Alpha
'''

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QColorDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QColor


class ColorPickerWidget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: Color Picker")

        self.go_home_callback = go_home_callback

        self._color = None
        self._default_color = None

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

        # the button for picking the color
        self.pick_btn = QPushButton("Pick Color")
        self.pick_btn.clicked.connect(self.open_color_picker)
        layout.addWidget(self.pick_btn)

        # 67676767676767766776767676776767 random labels...
        self.rgb_label = QLabel("No RGB selected")
        self.rgb_label.setWordWrap(True)

        self.hex_label = QLabel("No HEX selected")
        self.hex_label.setWordWrap(True)

        # rgb
        self.copy_rgb_btn = QPushButton("Copy RGB")
        self.copy_rgb_btn.setFixedWidth(100)
        self.copy_rgb_btn.clicked.connect(lambda: self.copy_output(self.rgb_label))

        # H E X !
        self.copy_hex_btn = QPushButton("Copy HEX")
        self.copy_hex_btn.setFixedWidth(100)
        self.copy_hex_btn.clicked.connect(lambda: self.copy_output(self.hex_label))

        rgb_layout = QHBoxLayout()
        rgb_layout.addWidget(self.rgb_label, 1)
        rgb_layout.addWidget(self.copy_rgb_btn)

        hex_layout = QHBoxLayout()
        hex_layout.addWidget(self.hex_label, 1)
        hex_layout.addWidget(self.copy_hex_btn)

        output_layout = QVBoxLayout()
        output_layout.addLayout(rgb_layout)
        output_layout.addLayout(hex_layout)

        layout.addLayout(output_layout)

        layout.addStretch(1)
        self.setLayout(layout)

    # go big or go home :sob:
    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()

    # Logic for the COLOR picker things
    def open_color_picker(self):
        dlg = QColorDialog(self)

        if self._color:
            dlg.setCurrentColor(QColor(self._color))

        if dlg.exec():
            color = dlg.currentColor()
            self.set_color(color)

    def set_color(self, color: QColor):
        self._color = color

        hex_value = color.name()
        rgb_value = f"rgb({color.red()}, {color.green()}, {color.blue()})"

        self.hex_label.setText(f"{hex_value}")
        self.rgb_label.setText(f"{rgb_value}")

    # CLIPBOARD copying stuff
    def copy_output(self, label):
        text = label.text()
        if text and text != "No color selected":
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(text)

PLUGIN = {
    "name": "Color Picker and Converter",
    "keywords": ["color", "picker", "converter", "rgb", "hex", "color code", "color picker"],
    "widget": ColorPickerWidget
}