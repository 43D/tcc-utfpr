import multiprocessing
import os
from PIL import Image
from pystray import Icon, Menu, MenuItem
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webview
from src.DB.DatabaseFactory import DatabaseFactory
from src.Api import Api
from src.Core.Windows.WindowsStartUp import WindowsStartUp
from src.Socket_pros.ProcessSocket import ProcessSocket

class MyHandler(FileSystemEventHandler):
    def __init__(self, func) -> None:
        super().__init__()
        self._func = func
    
    def on_created(self, event):
        if os.path.basename(event.src_path) == os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'PySocial', 'open.process'):
            with open(event.src_path, 'r') as f:
                print(f.read())
            os.remove(event.src_path)
            self._func(None, None)
            
def is_process_running(pid):
    try:
        res = psutil.pid_exists(pid)
        if res:
            return "pysocial.exe" in psutil.Process(pid).exe()
        return res
    except psutil.NoSuchProcess:
        return False
    
def run_webview(api_js, path):
    janela = webview.create_window('Py Social', "https://43d.github.io/tcc-utfpr/", js_api=api_js, min_size=(1270,630), confirm_close=True, text_select=True, zoomable=True)
    api_js.setWindow(janela)
    webview.start()
        

Process = multiprocessing.Process
Queue = multiprocessing.Queue    
webview_process = None
socket_process = None
path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'PySocial') 
if not os.path.exists(path):
    os.makedirs(path)
uid_file = os.path.join(path, 'uid.process') 
open_file = os.path.join(path, 'open.process') 

try:
    with open(uid_file, 'r') as f:
        pid_from_file = int(f.readline().strip())
except (FileNotFoundError, ValueError):
    pid_from_file = None
        
if __name__ == "__main__":
    multiprocessing.freeze_support()   
     
    WindowsStartUp(project_folder=os.path.dirname(os.path.realpath(__file__)))
    db = DatabaseFactory().create()
    db.setTagValueIfNotExit("path_sys", os.path.dirname(os.path.realpath(__file__)))
    
    def start_webview_process():
        path = os.path.join(db.getTagValue("path_sys")[1], 'view', 'index.html')
        global webview_process
        webview_process = Process(target=run_webview, args=(api_js, path, ))
        webview_process.start()

    def on_open(icon, item):
        global webview_process
        if not webview_process.is_alive():
            start_webview_process()

    def on_exit(icon, item):
        if os.path.isfile(uid_file):
            os.remove(uid_file)
        if os.path.isfile(open_file):
            os.remove(open_file)
        icon.stop()
        global webview_process
        webview_process.terminate()
        t.stop()
        observer.stop()
        global socket_process
        socket_process.terminate()
        os._exit(0)
        
    def start_socket_process():
        global socket_process
        socket_process = Process(target=t.loopPrint)
        socket_process.start()
    
    if pid_from_file is None or not is_process_running(pid_from_file):
        pid = os.getpid()
        with open(uid_file, 'a') as f:
            f.write(str(pid))
        try: os.remove(open_file)
        except: pass
        
        event = multiprocessing.Event()
    
        event_handler = MyHandler(func=on_open)
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
    
        api_js = Api(evt=event)
        t = ProcessSocket(evt=event)
        start_webview_process()
        start_socket_process()

        image_path = os.path.join(db.getTagValue("path_sys")[1], 'public', 'logo', 'logo.ico')
        image = Image.open(image_path)
        menu = Menu(MenuItem('Abrir PySocial', on_open), MenuItem('Sair', on_exit))
        icon = Icon('PySocial', image, menu=menu)
        
        observer.start()
        icon.run()
        
        webview_process.terminate()
        t.stop()
        socket_process.terminate()
        
    elif not pid_from_file is None and is_process_running(pid_from_file):
        with open(open_file, 'a') as f:
            f.write(str("true"))
        
        






        