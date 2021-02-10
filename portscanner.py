#!/usr/bin/env python3
#*-* coding:utf-8 -*-
import socket
from IPy import IP
import termcolor
import time

#Author: OctopusTR

def tara(hedef):
    ip_cv = ip_kontrol(hedef)
    print(termcolor.colored(('\n' + '[Açık Portlar Taranıyor] => ' + str(hedef)), 'red'))
    for port in range(1,65535): # 1 - 65535 arası port taranacak
        port_tara(ip_cv, port)

def ip_kontrol(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def banner_cek(s):
    return s.recv(1024)

def port_tara(ipadres, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipadres, port))
        try:
            banner = banner_cek(sock)            
            print('[+] Açık Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[*] Açık Port : ' + str(port))
    except:
        pass

print('[!!] Adresler Arasında (,) Kullanın.\n')
hedefler = input('[+] Taranacak Adresleri Girin: ')
if ',' in hedefler:
    for ip_add in hedefler.split(','):
        tara(ip_add.strip(' '))
else:
    tara(hedefler)