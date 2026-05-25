'''
## CapyUtilities: MarkdownFormatterWidget
Description: Minimalist markdown editor and previewer (LIVE PREVIEW updates 300 ms)
Status: Beta
'''
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QTextBrowser,
    QLabel,
    QHBoxLayout,
    QSplitter
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QGuiApplication

import markdown
class MarkdownFormatterWidget(QWidget):
    def __init__(self, go_home_callback=None):
        super().__init__()

        self.setWindowTitle("CapyUtilities: Markdown Formatter")
        self.go_home_callback = go_home_callback

        # Create Markdown parser ONCE
        self.md = markdown.Markdown(
            extensions=[
                "fenced_code",
                "tables",
                "toc"
            ]
        )

        layout = QVBoxLayout(self)

        # Back button
        back_button = QPushButton("← Back")
        back_button.setFixedSize(80, 30)
        back_button.clicked.connect(self.go_home)

        layout.addWidget(
            back_button,
            alignment=Qt.AlignmentFlag.AlignLeft
        )

        # Label
        layout.addWidget(QLabel("Markdown Input"))

        # Split view (Input on the left side, And preview on right side.)
        splitter = QSplitter(Qt.Orientation.Horizontal)

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText(
            "# Welcome to Markdown Formatter\n\n"
            "Type Markdown here..."
        )

        self.preview = QTextBrowser()
        self.preview.setOpenExternalLinks(True)

        splitter.addWidget(self.input_box)
        splitter.addWidget(self.preview)
        splitter.setSizes([500, 500])

        layout.addWidget(splitter)

        # Buttons
        button_layout = QHBoxLayout()

        self.copy_btn = QPushButton("Copy Markdown")
        self.copy_btn.clicked.connect(self.copy_markdown)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_all)

        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()

        layout.addLayout(button_layout)

        # Debounce timer
        self.preview_timer = QTimer(self)
        self.preview_timer.setSingleShot(True)
        self.preview_timer.timeout.connect(self.render_markdown)

        self.input_box.textChanged.connect(
            lambda: self.preview_timer.start(300)
        )

    def render_markdown(self):
        try:
            self.md.reset()

            html = self.md.convert(
                self.input_box.toPlainText()
            )

            self.preview.setHtml(html)

        except Exception as e:
            self.preview.setPlainText(
                f"Markdown Error:\n\n{e}"
            )

    def copy_markdown(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(
            self.input_box.toPlainText()
        )

    def clear_all(self):
        self.input_box.clear()
        self.preview.clear()

    def go_home(self):
        if self.go_home_callback:
            self.go_home_callback()


# Plugin data
PLUGIN = {
    "name": "Markdown Formatter",
    "keywords": [
        "markdown",
        "md",
        "formatter",
        "preview",
        "renderer"
    ],
    "widget": MarkdownFormatterWidget
}