import json
import os
import multiprocessing
import requests
import socketio
from src.Cript.CryptData import CryptData
from src.DB.DatabaseFactory import DatabaseFactory


class ProcessSocket:
    def __init__(self,  evt: multiprocessing.Event) -> None:
        self.loop = True
        self._evt=evt
        self.sio = socketio.Client()
        self._url_login = "http://127.0.0.1:5011/v1/cliente/login/" #191.101.70.171:5011
        self._log = []

    def _get_token(self, user, password)-> str:
        payload = json.dumps({
            "password": password,
            "user": user
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", self._url_login, headers=headers, data=payload)

        res = json.loads(response.text)
        token = res.get("token")

        response = requests.request("PUT", self._url_login, headers={'Authorization': f"Bearer {token}"}, data={})
        
        return token
    
    def _getLoginInformation(self):
        res = self._db.getUser()
        if res:
            user = {
                "username": self._crypt.get_decode(res[0][0]), 
                "password": self._crypt.get_decode(res[0][1])
            }
            return user
        return None
    
    def loopPrint(self):
        self._db = DatabaseFactory().create()
        self._crypt = CryptData()
        while self.loop == True:
            user = self._getLoginInformation()
            if user:
                token = self._get_token(user=user.get("username"), password=user.get("password"))
                print("123")
                intervalo = int(self._db.getTagValue("IntervaloColetorXML")[1])
                try:
                    self.connect_socket(username=user.get("username"), token=token)
                    print("send file", self.sio.connected)
                except Exception as e:
                    print("error:", e)
                    
            self._evt.wait((intervalo + 1) * 60)
            self._evt.clear()

    def stop(self):
        self.loop = False
        
    def _disconect_socket(self):
        self.sio.disconnect()
        
    def _send_file(self):
        file = "Z:\\image.jpg"
        with open(file, 'rb') as f:
            data = f.read()
        self.sio.emit("send_file", {"file": data, "name": "465465465.jpg", "cnpj": 5454545}, callback=self._disconect_socket)
    
    def _process_data(self):
        arquivos_xml = []
        db = DatabaseFactory().create()
        paths = db.getAllPathColetorXML()
        
        for diretorio in paths:
            for raiz, dirs, arquivos in os.walk(diretorio[1]):
                for arquivo in arquivos:
                    if arquivo.endswith('.xml'):
                        arquivos_xml.append(os.path.join(raiz, arquivo))
        print(arquivos_xml)

    def connect_socket(self, username, token):
        @self.sio.event
        def connect():
            print("Conexão bem-sucedida!")
            self._process_data()

        @self.sio.event
        def connect_error(er):
            print("Erro na conexão!", er)

        @self.sio.event
        def disconnect():
            print("Desconectado!")
            
        print(token, username)
        if not self.sio.connected:
            self.sio.connect('http://127.0.0.1:5011', headers={
                "token": token,
                "username": username,
                "type": "EXTERNO"
            }, wait_timeout= 10)
            