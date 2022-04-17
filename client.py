import socket

host = socket.gethostname()
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
    print("Socket establecido")
    socket_cliente.connect((host, port))
    print("Socket conectado")
