# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Annex.py', 'background.mp3', 'beep.wav', 'bgimg.jpg', 'camera-shutter-click.mp3', 'Commands', 'List.txt', 'defaultFace4.ico', 'explosion.mp3', 'gmov.jpg', 'Google', 'Assitant', 'Voice.py', 'Heisenberg.db', 'Heisenberg.ico', 'Heisenberg.py', 'Heisenberg.spec', 'Insertion.py', 'Mic.png', 'PasswordGenerator.ico', 'PyWhatKit_DB.txt', 'pywhatkit_dbs.txt', 'quarter', 'spin', 'flac.mp3', 'README.md', 'setting.ico', 'Snake.py', 'text_to_speech.ico', 'wlcm.jpeg'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Annex',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
