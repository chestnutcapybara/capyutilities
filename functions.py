import sys
from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase

def resolve_path(relative_path: str) -> Path:
    meipass = getattr(sys, "_MEIPASS", None)
    
    if meipass:
        base_path = Path(meipass)
    else:
        base_path = Path(__file__).parent.resolve()

    return base_path / relative_path

def load_custom_font(font_filename: str) -> str:
    path = str(resolve_path(font_filename))
    
    #Load into the Qt Font Database
    font_id = QFontDatabase.addApplicationFont(path)
    
    if font_id == -1:
        raise RuntimeError(f"Could not load font: {font_filename}")
        
    # Extract the family name from the loaded font
    families = QFontDatabase.applicationFontFamilies(font_id)
    if not families:
        raise RuntimeError(f"No font families found in: {font_filename}")
        
    return families[0]