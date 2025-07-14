#!/usr/bin/env python3
import os

os.system("clear")
os.system("figlet MRZBSCS")

while True:
    print("""
    
    MRZBSCS Aracına Hoş Geldiniz:
    
    1) Hızlı Port Tarama (nmap)
    2) Servis Ve Sistem Bilgisi (nmap)
    3) İşletim Sistemi Bilgisi (nmap)
    4) Zafiyet Tarama (nikto)
    5) Exploit Arama (searchsloit)
    
    """)
    islemno = input("İşlem Numarası Giriniz: ")
    if islemno == "1":
        hedef_ip = input("Hedefe IP Giriniz: ")
        os.system("nmap {}".format(hedef_ip))

    elif islemno == "2":
        hedef_ip = input("Hedefe IP Giriniz: ")
        os.system("nmap -sS -sV {}".format(hedef_ip))

    elif islemno == "3":
        hedef_ip = input("Hedefe IP Giriniz: ")
        os.system("nmap -O --fuzzy {}".format(hedef_ip))

    elif islemno == "4":
        hedef_ip = input("Hedefe IP Giriniz: ")
        os.system("nikto -h {}".format(hedef_ip))

    elif islemno == "5":
        anahtarkelime = input("Anahtarkelime Giriniz: ")
        os.system("searchsloit {}".format(anahtarkelime))

    else:
        print("Hatalı giriş")