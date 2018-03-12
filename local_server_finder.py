#!/usr/bin/python3
import time
import socket
import requests


def get_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_string = s.getsockname()[0]
    s.close()
    return ip_string


my_ip = get_local_ip_address()
omit_last_octet = '.'.join(my_ip.split('.')[:-1])
i = 0
while 1:
    try:
        print(
            f"{omit_last_octet}.{i} - Status Code: {requests.request('GET', f'http://{omit_last_octet}.{i}:11111', timeout=5).status_code}")
    except:
        print(f'{omit_last_octet}.{i} - Unable to fetch response')
    i += 1
    time.sleep(1)
