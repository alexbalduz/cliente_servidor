import socket
import threading

class servidor():
    host = socket.gethostname()
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
        socket_server.bind((host, port))
        socket_server.listen(5)

        print("\nSocket establecido")

        conexion_socket, direccion = socket_server.accept()

        print("Primera conexion : ", direccion[0])