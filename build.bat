@echo off
python -m nuitka ^
    --standalone ^
    --jobs=10 ^
    --show-progress ^
    --windows-console-mode=disable ^
    --plugin-enable=pyside6 ^
    --include-qt-plugins=platforms ^
    --windows-icon-from-ico=icon.ico ^
    --noinclude-qt-translations ^
    --remove-output ^
    main.py
pause