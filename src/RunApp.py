import os
import psutil
import webview
from src.Api import Api

class RunApp:
    def __init__(self, api: Api, exe: str = "PySocial.exe", url: str = "http://localhost:5173/tcc-utfpr", debug: bool = False, debug_tool: bool = False) -> None:
        self._exe = exe
        self._url = url
        self._debug = debug
        self._debug_tool = debug_tool
        self._api_js = api

    def _start_webview_process(self):
        webview.create_window('Py Social', url=self._url, js_api=self._api_js, min_size=(1270,680), confirm_close=True, text_select=True, zoomable=True)
        webview.settings = {
            'ALLOW_DOWNLOADS': True,
            'ALLOW_FILE_URLS': True,
            'OPEN_EXTERNAL_LINKS_IN_BROWSER': True,
            'OPEN_DEVTOOLS_IN_DEBUG': self._debug_tool,
            "REMOTE_DEBUGGING_PORT": None,
            'IGNORE_SSL_ERRORS': True
        }
        webview.start(debug=self._debug_tool, gui='edgechromium', private_mode=False)
            
    def _on_exit(self):
        os._exit(0)

    def _is_app_running(self):
        count = sum(1 for proc in psutil.process_iter(['name']) if proc.info['name'] == self._exe)
        return count > 1  # Retorna True se houver mais de uma instância

    def run(self):
        if self._is_app_running():
            return self._on_exit()
        self._start_webview_process()
