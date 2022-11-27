import optparse

def is_ip_adress(ip):
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
    parser.add_option("-t" , "--th" , dest = "threads" , help = "Number of threads , for default 100000")
    arguments , options = parser.parse_args()
    if not arguments.ip:
        parser.error("[-] Please set IP adress of target , for more information use --help")
    if not arguments.threads:
        arguments.threads = 100000
    return (arguments.ip , arguments.threads)

def parse_args() :
    get_ip , number_threads = get_arguments()
    if is_ip_adress(get_ip):
        pass
    else:
        print("[-] Inccorect ip adress")
        exit()
    try:
        number_threads = int(number_threads)
    except:
        print("[-] Inccorect number of threads")
    if (number_threads <= 0):
        print("[-] Number of threads must be >= 0")
        exit()
    return (get_ip , number_threads)