# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\python_projects\\project_nagiubtal\\nagiubtal_accounts.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\python_projects\\project_nagiubtal\\prices.json', '.'), ('D:\\python_projects\\project_nagiubtal\\pathes.spec', '.'), ('D:\\python_projects\\project_nagiubtal\\project_tools', 'project_tools/'), ('D:\\python_projects\\project_nagiubtal\\dlls', 'dlls/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='nagiubtal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
