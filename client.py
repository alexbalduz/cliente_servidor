from concurrent.futures import thread
import socket
import threading

class hilo_cliente(threading.Thread):
    def __init__ (self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            data = self.socket.recv(2048)
            dt = data.decode()
            if(dt == ''):
                continue
            print(dt)

class cliente():
    def iniciar():
        host = socket.gethostname()
        port = 12345

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
            print("Socket establecido")
            socket_cliente.connect((host, port))
            print("Socket conectado")
            hl = hilo_cliente(socket_cliente)
            hl.start()
            while True:
                data = input('Escribe algo > ')
                dt = bytes(data, 'UTF-8')
                socket_cliente.send(dt)
