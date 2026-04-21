### Imports ###

# Qt imports

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QLineEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# System imports
import sys
from typing import NoReturn

# Local imports
import functions

### Main Window Class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bingy Utilities')
        self.setMinimumSize(400, 300)

        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header
        title_label = QLabel('Bingy Utilities')
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Search Area
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search tools...')
        self.search_bar.setMinimumHeight(40)
        main_layout.addWidget(self.search_bar)

        # Quick Access Section
        main_layout.addWidget(QLabel('Quick Access:'))
        
        button_layout = QHBoxLayout()
        self.btn_action = QPushButton('Run Utility')
        self.btn_clear = QPushButton('Clear Search')
        
        button_layout.addWidget(self.btn_action)
        button_layout.addWidget(self.btn_clear)
        main_layout.addLayout(button_layout)

        # Signals
        self.btn_action.clicked.connect(self.on_run_click)
        self.btn_clear.clicked.connect(lambda: self.search_bar.clear())

        # Spacer to push everything to the top
        main_layout.addStretch()

    def on_run_click(self):
        query = self.search_bar.text()
        print(f"Executing utility for: {query if query else 'Default Tool'}")

def main() -> NoReturn:
    app = QApplication(sys.argv)

    ## Load Font ##
    try:
        # Load both there's also bold
        font_family = functions.load_custom_font("DMSans-Regular.ttf")
        functions.load_custom_font("DMSans-Bold.ttf")

        # Set the global font for the whole app
        app.setFont(QFont(font_family, 11))
        
    except RuntimeError as e:
        print(f"Font Error: {e}")


    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()