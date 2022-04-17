import socket
import threading

class hilo_servidor(threading.Thread):
    def __init__(self,conexion,direccion, sockets):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion
    def run(self):
        print("\nNew conexion : ", self.direccion[0])
        while True:
            data = self.conexion.recv(2048)
            dt = data.decode()
            if dt == '':
                continue
            print(self.direccion[0], " > ", dt)
class servidor():
    def iniciar():
        host = socket.gethostname()
        port = 12345
        hilos = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
            socket_server.bind((host, port))
            socket_server.listen(5)

            print("\nSocket establecido")
            print("\nEsperando...")

            while True:
                conexion_socket, direccion = socket_server.accept()
                hilo = hilo_servidor(conexion_socket, direccion)
                hilo.start()
                hilos.append(hilo)
servidor.iniciar()