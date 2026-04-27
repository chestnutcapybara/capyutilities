from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QSizePolicy
)

class CapitalizationWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bingy Utilities: Capitalization Tool")

        layout = QVBoxLayout()

        # Add spacing between UI Elements
        layout.addSpacing(10)

        # Input box
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text here...")
        self.input_text.setFixedHeight(30)

        self.input_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Output label
        self.output_label = QLabel("Formatted text will appear here")
        self.output_label.setWordWrap(True)

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
        layout.addWidget(self.output_label)

        layout.addStretch(1)
        self.setLayout(layout)

    def get_text(self):
        return self.input_text.toPlainText()

    def to_upper(self):
        self.output_label.setText(self.get_text().upper())

    def to_title(self):
        self.output_label.setText(self.get_text().title())

    def to_lower(self):
        self.output_label.setText(self.get_text().lower())


# Plugin data
PLUGIN = {
    "name": "Capitalization Tool",
    "keywords": ["caps", "uppercase", "lowercase", "title", "text"],
    "widget": CapitalizationWidget
}