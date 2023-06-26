import socket

def check_port(host, port):
    try:
        sock = socket.create_connection((host, port), timeout=1)
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

host = 'localhost'
port = 7687

if check_port(host, port):
    print(f"El puerto {port} está abierto en {host}")
else:
    print(f"El puerto {port} está cerrado en {host}")