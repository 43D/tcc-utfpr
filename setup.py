import os
from cx_Freeze import setup, Executable

def tree(src):
    return [
        (root, list(map(lambda f: os.path.join(root, f), files)))
        for (root, dirs, files) in os.walk(os.path.normpath(src))
    ]

def lista(src):
    data = []
    obj = tree(src)
    for root, files in obj:
        for file in files:
            dest = os.path.join(src, os.path.relpath(file, src))
            data.append((file, dest))
    return data

includefiles = lista('view') + lista('public')
print(includefiles)
packages = ["webview", "pystray","PIL", 'psutil', 'watchdog']

op = {
    'include_files': includefiles,
    "packages": packages,   
}
exe = Executable(
    script="app.py",
    base="Win32GUI",
    target_name="pysocial.exe"
)

setup(
    name="PySocial",
    version="0.1.0",
    description="Aplicativos desc...",
    options = {'build_exe': op},
    executables=[exe],
)
