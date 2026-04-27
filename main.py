### Imports ###

# Qt imports

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QLineEdit, QStackedWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# System imports
import sys
from typing import NoReturn

# Local imports
import functions
import plugin_loader

### Main Window Class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bingy Utilities')
        self.setMinimumSize(400, 300)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create start page
        self.start_page = self.build_start_page()
        self.stack.addWidget(self.start_page)

        self.plugins = plugin_loader.load_plugins()
        print(f"Loaded plugins: {[p['name'] for p in self.plugins]}") # Debug info

    def open_plugin(self, plugin):
        widget_class = plugin["widget"]
        widget = widget_class(go_home_callback=self.go_home)

        self.stack.addWidget(widget)
        self.stack.setCurrentWidget(widget)


    def build_start_page(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel('Bingy Utilities')
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search tools...')
        self.search_bar.setMinimumHeight(40)
        self.search_bar.returnPressed.connect(self.on_run_click)
        layout.addWidget(self.search_bar)

        button_layout = QHBoxLayout()
        self.btn_action = QPushButton('Run Utility')
        self.btn_clear = QPushButton('Clear Search')

        button_layout.addWidget(self.btn_action)
        button_layout.addWidget(self.btn_clear)
        layout.addLayout(button_layout)

        self.btn_action.clicked.connect(self.on_run_click)
        self.btn_clear.clicked.connect(lambda: self.search_bar.clear())

        layout.addStretch()

        return widget
    
    def go_home(self):
        self.stack.setCurrentWidget(self.start_page)

    def on_run_click(self):
        query = self.search_bar.text().lower()

        for plugin in self.plugins:
            if query in plugin["name"].lower() or any(query in k for k in plugin["keywords"]):
                self.open_plugin(plugin)
                return

        print("No matching utility found")

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