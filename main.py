#!/usr/bin/env python3
import os

os.system("apt-get install figlet")
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
    6) Firewall Tespit (wafw00f)
    7) Brute Force Attack FTP (ncrack)
    8) Brute Force SSH (ncrack)
    9) Brute Force Telnet (ncrack)
    10) Brute Force HTTP (ncrack)
    11) Brute Force SMB (ncrack)
    12) Brute Force RDP (ncrack)
    13) Brute Force SIP (ncrack)
    14) Brute Force Redis (ncrack)
    15) Brute Force VNC (ncrack)
    16) Brute Force PostgreSQL (ncrack)
    17) Brute Force MySQL (ncrack)

    """)
    islemno = input("İşlem Numarası Giriniz: ")
    if islemno == "1":
        hedef_ip = input("Hedef IP Giriniz: ")
        os.system("nmap {}".format(hedef_ip))

    elif islemno == "2":
        hedef_ip = input("Hedef IP Giriniz: ")
        os.system("nmap -sS -sV {}".format(hedef_ip))

    elif islemno == "3":
        hedef_ip = input("Hedef IP Giriniz: ")
        os.system("nmap -O --fuzzy {}".format(hedef_ip))

    elif islemno == "4":
        hedef_ip = input("Hedef IP Giriniz: ")
        os.system("nikto -h {}".format(hedef_ip))

    elif islemno == "5":
        anahtarkelime = input("Anahtar Kelime Giriniz: ")
        os.system("searchsloit {}".format(anahtarkelime))

    elif islemno == "6":
        siteaddress = input("Site Adresi Giriniz: ")
        os.system("wafw00f {}".format(siteaddress))

    elif islemno in ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]:
        hedef_ip = input("Hedef IP Giriniz: ")
        username = input("Username Giriniz: ")
        password = input("Password Dosya Pathi Giriniz: ")

        port_haritasi = {
            "7": "21",   # FTP
            "8": "22",   # SSH
            "9": "23",   # Telnet
            "10": "80",  # HTTP
            "11": "445", # SMB
            "12": "3389",# RDP
            "13": "5060",# SIP
            "14": "6379",# Redis
            "15": "5900",# VNC
            "16": "5432",# PostgreSQL
            "17": "3306" # MySQL
        }

        secilen_port = port_haritasi[islemno]
        os.system("ncrack -p {} -u {} -P {} {}".format(secilen_port, username, password, hedef_ip))

    elif islemno == "18":
        hedef_ip = input("Hedef IP Giriniz: ")

    else:
        print("Hatalı giriş")
