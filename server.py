import socket
from decouple import config as env

HOST = env('LOCALHOST')
PORT = env('PORT')


class Server:

    def __init__(self) -> None:
        # AF_INET socket type for IPV4, SOCK_STREAM socket type for tcp
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            with self.tcp as tcp:
                tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                tcp.bind((HOST, int(PORT)))
                tcp.listen()
                print(f"Servidor Online, escutando a porta {PORT}")
                while True:
                    connection, client = tcp.accept()
                    print(f"Conexão estabelecida com o cliente: {client}")
                    while True:  # Recebe diversos clientes
                        msg = connection.recv(1024)
                        print(f"Enviando {msg} bytes para o cliente: {client}")
                        if not msg:
                            break
                        print(client, msg)
                    print('Finalizando conexao do cliente')
                    connection.close()
        except KeyboardInterrupt:
            print('Finalizando servidor!')


if __name__ == "__main__":
    server = Server()
    server.run()
