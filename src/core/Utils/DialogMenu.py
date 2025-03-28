import webview

class DialogMenu:
    def save_file_dialog(self, type_file: str = "file", filename: str = "nome") -> str | None:
        if len(webview.windows) < 0: return
        res = webview.windows[0].create_file_dialog(
            webview.SAVE_DIALOG, directory='/', save_filename=f"{filename}.{type_file}"
        )
        if res is not None:
            if not res.endswith(f".{type_file}"):
                res += f".{type_file}"
        return res