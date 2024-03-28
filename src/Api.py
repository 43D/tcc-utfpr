import multiprocessing
import os
from src.Cript.CryptData import CryptData
from src.DB.DatabaseFactory import DatabaseFactory
import webview

class Api:
    def __init__(self, evt: multiprocessing.Event) -> None:
        self._evt=evt
        self._crypt = CryptData()
        
    def setWindow(self, w : webview.Window):
        self._window = w
    
    def verificarArquivoAgora(self):
        self._evt.set()
        
    def getLoginInformation(self):
        db = DatabaseFactory().create()
        res = db.getUser()
        user = {
            "username": "", 
            "password": ""
        }
        if res:
            user["username"] = self._crypt.get_decode(res[0][0])
            user["password"] = self._crypt.get_decode(res[0][1])
        return user
   
    def setLoginInformation(self, obj: dict):
        db = DatabaseFactory().create()
        res = db.getUser()
        username = self._crypt.get_encode(obj["username"])
        password = self._crypt.get_encode(obj["password"])
        if res:
            db.updateUser(password=password, username=username, id=res[0][2])
        else: 
            db.setUser(password=password, username=username)
            
    def getConfingColetorXML(self):
        db = DatabaseFactory().create()
        coletor = db.getTagValue("ColetorXML")[1]
        status = db.getTagValue("IntervaloColetorXML")[1]
        list_path = db.getAllPathColetorXML()
        paths = []
        for path in list_path:
            paths.append({
                "id": path[0],
                "path": path[1]
            })
        
        obj = {
            "coletorXML": coletor,
            "intervaloColetorXML": status,
            "path": paths
        }
        
        return obj
    
    def setConfingColetorXML(self, obj: dict):
        try: 
            print(obj)
            db = DatabaseFactory().create()
            db.setTagValue("ColetorXML", obj.get("coletorXML"))
            db.setTagValue("IntervaloColetorXML", obj.get("intervaloColetorXML"))
            db.replaceAllPathColetorXML(obj.get("path"))
            return True
        except Exception as e:
            print("api", e)
            return False
    
    def selecionar_pasta(self):
        resultado = self._window.create_file_dialog(webview.FOLDER_DIALOG)
        if resultado: 
            return resultado[0]  
        else:
            return None 

    def saveEmpresas(self, data: list[dict]):
        lista_cryp = []
        for empresa in data:
            t = (
                empresa.get("id"),
                self._crypt.get_encode(empresa.get("nome")),
                self._crypt.get_encode(empresa.get("cnpj")),
                self._crypt.get_encode(empresa.get("razao_social")),
                self._crypt.get_encode(empresa.get("junta_comercial")),
                self._crypt.get_encode(empresa.get("apelido")),
                self._crypt.get_encode(empresa.get("nome_fantasia")),
                empresa.get("cidade_id")
            )
            lista_cryp.append(t)
        db = DatabaseFactory().create()
        db.replaceAllEmpresas(lista=lista_cryp)

    def openFolder(self, path):
        os.startfile(path)

    def setStartUpWindows(self, status):
        pass
    
    def getStartUpWindows(self):
        pass
