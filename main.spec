# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
    'PySide6.QtNetwork',
    'PySide6.QtSql',
    'PySide6.QtXml',
    'PySide6.QtDBus',
    'PySide6.QtBluetooth',
    'PySide6.QtNfc',
    'PySide6.QtPdf',
    'PySide6.QtPdfWidgets',
    'PySide6.QtPrintSupport',  
    'PySide6.QtSvg',          
    'PySide6.QtOpenGL',        
    'PySide6.QtOpenGLWidgets',
    'PySide6.QtTest',
    'PySide6.QtSensors',
    'PySide6.QtPositioning',
    'PySide6.QtRemoteObjects',
    'PySide6.QtWebChannel',
    'PySide6.QtWebEngineCore',
    'PySide6.QtWebEngineWidgets',
    'PySide6.QtQuick',
    'PySide6.QtQml',
    'PySide6.QtCharts',
    'PySide6.Qt3DCore',
    'PySide6.QtMultimedia',
    'PySide6.QtMultimediaWidgets',
    ],
    noarchive=False,
    optimize=2,
)
useful_binaries = []
for (dest, source, kind) in a.binaries:
    # Drop translations 
    if 'translations' in dest.lower():
        continue
    # Drop large DLLs
    if 'Qt6Network' in dest or 'Qt6Sql' in dest or 'Qt6Xml' in dest:
        continue
    if 'libEGL' in dest or 'libGLESv2' in dest or 'opengl32sw' in dest:
        continue
    useful_binaries.append((dest, source, kind))

a.binaries = useful_binaries

files_to_remove = [
    'Qt6Network',      # Networking (Huge)
    'Qt6Pdf',          # PDF rendering
    'Qt6Svg',          # SVG support
    'opengl32sw.dll',  # Software OpenGL renderer (approx. 10MB!)
    'D3DCompiler_47',  # DirectX compiler (approx. 4MB)
    'translations',    # All non-English language files
]

a.binaries = [x for x in a.binaries if not any(bad in x[0] for bad in files_to_remove)]
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
