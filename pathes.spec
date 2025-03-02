# -*- mode: python -*-
a = Analysis(
    ['nagiubtal_accounts.py'],  # Replace with your project's main script
    pathex=['D:\python projects\project nagiubtal'],
    hiddenimports=[],
    hookspath=None,
    runtime_hooks=None,
    # Add your assets here
    datas=[('D:\python projects\project nagiubtal\project_tools', 'project_tools')],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,  # This includes the assets in the build
    name='nagiubtal_accounts.exe',  # Replace with your desired output executable name
    debug=False,
    strip=None,
    upx=True,
    console=True,
    icon='icon.ico'  # Replace with your custom icon if needed
)
