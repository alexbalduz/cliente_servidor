import socket

host = socket.gethostname()
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
    print("Socket establecido")
    socket_cliente.connect((host, port))
    print("Socket conectado")
    while True:
        data = input('Escribe algo > ')
        dt = bytes(data, 'UTF-8')
        socket_cliente.send(dt)
