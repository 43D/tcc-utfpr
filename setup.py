import os
from cx_Freeze import setup, Executable
import pkg_resources

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
            dest = os.path.join(src, os.
            path.relpath(file, src))
            data.append((file, dest))
    return data

includefiles = lista('view')
packages = ["webview", "psutil", "cryptography"]

op = {
    'include_files': includefiles,
    "packages": packages,   
    'add_to_path': True,
    'include_msvcr': True,
}

exe = Executable(
    script="app.py",
    icon="view\\icon.ico",
    base="Win32GUI",
    target_name="PySocial.exe"
)

setup(
    name="PySocial",
    version="0.0.1",
    description="Py Social",
    options = {'build_exe': op},
    executables=[exe],
)