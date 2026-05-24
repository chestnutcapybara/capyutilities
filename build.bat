@echo off
python -m nuitka ^
    --standalone ^
    --jobs=10 ^
    --show-progress ^
    --plugin-enable=pyside6 ^
    --include-qt-plugins=platforms ^
    --windows-icon-from-ico=icon.ico ^
    --noinclude-qt-translations ^
    --remove-output ^
    --include-data-files=DMSans-Regular.ttf=DMSans-Regular.ttf ^
    --include-data-files=DMSans-Bold.ttf=DMSans-Bold.ttf ^
    --include-raw-dir=widgets=widgets ^
    --include-data-files=icon.ico=icon.ico ^
    main.py
pause