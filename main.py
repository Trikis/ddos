import threading
import src.args as args
import src.simple_variant as simple_variant


def main_work():
    ip_arg , threads_number = args.parse_args()
    thread_arr = []
    for i in range(threads_number):
        thread_arr.append(threading.Thread(target = simple_variant.odnop , args = (ip_arg , )))

    for curr_thread in thread_arr:
        curr_thread.start()

if __name__ == "__main__":
    main_work()
    