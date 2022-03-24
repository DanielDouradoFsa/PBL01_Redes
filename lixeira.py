from client import Client


class Lixeira(Client):

    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.capacity = capacity
        self.usage = 0
        self.isLocked = False
        self.message = ""

    def create_msg(self):  # overwrite method
        return {"capacity": self.capacity, "usage": self.usage, "isLocked": self.isLocked, "message": self.message}

    def fill(self, value: int):  # fills the laystall
        if self.isLocked:
            self.message = "Lixeira fechada"
        elif value <= self.capacity - self.usage:
            self.usage += value
            if self.usage == self.capacity:
                self.lock()
                self.message = "Lixeira ficou cheia"
            self.message = "Lixo Inserido"
            self.send_msg()

    def clear(self):  # clear the usage of laystall
        self.usage = 0
        self.message = "Lixo Coletado!"
        self.send_msg()

    def lock(self):
        self.isLocked = True
        self.message = "Lixo Trancada!"
        self.send_msg()

    def unlock(self):
        self.isLocked = False
        self.message = "Lixeira Destravada"
        self.send_msg()
