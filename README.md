# 🧰 CapyUtilities

Desktop utility with useful tools, converters, and mini-apps (all in one place, created with PySide6)

CapyUtilities is designed to be lightweight, modular, and easy to extend with plugins. 

---

## Features

- **Plugin-based architecture**  
  Add new utilities without touching core code

- **Modular tools system**  
  Each utility runs as its own widget

- **Home dashboard**  
  Quickly switch between tools using the main window.

- **Widgets**  
  Handy everyday tools like:
  - QR Code Creater
  - Base64 Encoder & Decoder
  - Color picker / RGB ↔ HEX converter
  - Markdown Formatter

## Create your own Plugins
1. To create or remove plugins from CapyUtilities, create a new file in the widgets/ directory, which will have many plugins inside already.
2. Then, copy everything from _template.py for the basic framework template for a Plugin into your new file.
3. Modify the template, renaming the main class and editing the PLUGIN dictionary at the bottom (Important)!
4. Do whatever you'd like and create an awesome new Plugin
