@echo off
python -m nuitka ^
    --standalone ^
    --onefile ^
    --lto=yes ^
    --jobs=10 ^
    --show-progress ^
    --windows-console-mode=disable ^
    --plugin-enable=pyside6 ^
    --include-qt-plugins=platforms ^
    --windows-icon-from-ico=icon.ico ^
    --noinclude-qt-translations ^
    --python-flag=no_docstrings,no_asserts ^
    --remove-output ^
    --clean-cache=all ^
    main.py
pause