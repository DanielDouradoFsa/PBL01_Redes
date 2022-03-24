import socket
from decouple import config as env
import json

HOST = env('LOCALHOST')
PORT = env('PORT')

class Client:#Base class for all Clients, Laystalls, Trucks, etc
    
    def __init__(self) -> None:
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):   
        self.tcp.connect((HOST, int(PORT)))

    def create_msg(self):
        return {}
    
    def send_msg(self):
        self.tcp.send(str.encode(json.dumps(self.create_msg())))
