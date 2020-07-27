#!usr/bin/python3
#_______________IMPORTS______________
import ipaddress
import socket
import os
import time
from os import name
import threading
import random

#___________________________FUNCTIONS__________________________
#                       !!!DO NOT TOUCH!!!
def testPort(targIP, port):
    newsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    newsock.settimeout(1)
    success = newsock.connect_ex((str(targIP), int(port)))
    if success == 0:
        banner = ""
        bannerprint = ""
        if str(port) in namedport:
            portname = namedport[str(port)]
        else:
            portname = ""
        try:
            banner = str(newsock.recv(1024).decode('utf-8'))
            cleanbanner = banner.strip("b'").rstrip("\r\n")
            bannerprint = (f" as {cleanbanner}")
        except:
            pass

        exploitDict[targIP] += f"\n    {portname} | {str(port)}{bannerprint}"
        print(f"    IP {str(targIP)}:{portname} Port {str(port)} is open{bannerprint}.")
    
    newsock.close()
    randStart = round(100 * ((-1 * obfuscationStagger) - 1))
    randFin = round(100 * (obfuscationStagger + 1))
    staggeringPercent = random.randrange(randStart, randFin)
    time.sleep(max(0, ((speed / 1000)*(staggeringPercent/100))))
def testIP(targIP):
    if name == 'nt':
        ifPresent = os.system(f"ping -n 1 -w {iPingWait} {str(targIP)} >nul 2>nul")
    else:
        ifPresent = os.system(f"ping -c 1 -i {iPingWait} {str(targIP)} >/dev/null")
    if ifPresent == 0:
        exploitDict[targIP] = "\n    Is active."
        if len(inp) == 0:
            for count in range(0, 65536):
                if isMultithread == True:
                    wildThread = threading.Thread(target=testPort, args=(targIP, count))
                    wildThread.start()
                    if count % sailors == 0:
                        wildThread.join()
                else:
                    testPort(targIP, count)
            wildThread.join()

        elif "-" in inp[0]:
            if isMultithread == True:
                firstport, lastport = (str(inp[0])).split('-')
                for port in range(int(firstport), (int(lastport) + 1)):
                    wildThread = threading.Thread(target=testPort, args=(targIP, port))
                    wildThread.start()
                wildThread.join()
            else:
                firstport, lastport = (str(inp[0])).split('-')
                for port in range(int(firstport), (int(lastport) + 1)):
                    testPort(targIP, port)

        elif "t20" in inp[0]:
            top20 = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
            if isMultithread == True:
                for port in top20:
                    wildThread = threading.Thread(target=testPort, args=(targIP, port))
                    wildThread.start()
                wildThread.join()
            else:
                for port in top20:
                    testPort(targIP, port)
        else:
            for count in inp:
                if isMultithread == True:
                    wildThread = threading.Thread(target=testPort, args=(targIP, count))
                    wildThread.start()
                    if count % sailors == 0:
                        wildThread.join()
                else:
                    testPort(targIP, count)
def GUI():
    clear()
    print("\n\n\n")
    print("████████╗██████╗░░█████╗░███████╗░█████╗░██╗░░░░░░██████╗░░█████╗░██████╗░")
    print("╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░░░██╔════╝░██╔══██╗██╔══██╗")
    print("░░░██║░░░██████╔╝███████║█████╗░░███████║██║░░░░░██║░░██╗░███████║██████╔╝")
    print("░░░██║░░░██╔══██╗██╔══██║██╔══╝░░██╔══██║██║░░░░░██║░░╚██╗██╔══██║██╔══██╗")
    print("░░░██║░░░██║░░██║██║░░██║██║░░░░░██║░░██║███████╗╚██████╔╝██║░░██║██║░░██║")
    print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝")
    GUITypeName()
    print("----------------------------------v0.110---------------------------------")
    print(f"{randomMessage()}\n\n")
    print("OpTest: scanme.nmap.org | hackthissite.org")
    print("Check file for config.")
    print("\n")
    print(f"Captains: {captains} | Sailors Per Crew: {sailors}")
    print(f"Target: {target} | Delay: {speed}ms | Obfuscation Stagger: {obfuscationStagger} | Ports: {inp}")
def clear():
    if name == 'nt':
        os.system('cls')

    else:
        os.system('clear')
def GUITypeName():
    if typechoice == 0:
        print("░░░░░░░░░░░░░░░░░░░░░░█▀█ █▀█ █▀█ ▀█▀ █▀ █▀▀ ▄▀█ █▄░█░░░░░░░░░░░░░░░░░░░░")
        print("░░░░░░░░░░░░░░░░░░░░░░█▀▀ █▄█ █▀▄ ░█░ ▄█ █▄▄ █▀█ █░▀█░░░░░░░░░░░░░░░░░░░░")
def randomMessage():
    guiRand = random.randrange(1, 7)
    if guiRand == 1:
        guiMessage = "----------------------~~Now with multithreading!~~-----------------------"
    elif guiRand == 2:    
        guiMessage = "-------------------------~~On the offensive!~~---------------------------"
    elif guiRand == 3:    
        guiMessage = "---------------------------~~Kismet, Hardy.~~----------------------------"
        #Kismet's actually a mishearing. Historians figure he said, "Kiss me, Hardy," or
        #"Kiss Emma, Hardy". Victorian historians wrongly assumed that he meant "Kismet" after
        #the Turkish word for 'destiny', but no Turkish was in the english lexicon at the time.
    elif guiRand == 4:    
        guiMessage = "------------------~~Don't throw me overboard, Hardy.~~-------------------"
    elif guiRand == 5:    
        guiMessage = "-------------------~~Thank God I have done my Duty.~~--------------------"
    elif guiRand == 6:    
        guiMessage = "---------------~~What do you do with a drunken sailor?!~~----------------"
    return(guiMessage)

#_________________________CONFIGURATION________________________
#Feel free to mess with anything in the config.


#Trafalgar currently operates on Windows Powershell and most Linux builds. Could work on Mac. Run with python3.

iPingWait = 1 #How long the ping waits before calling it a lost cause.
captains = 8 #Maximum Number of IP thread workers. Pushing it may turn
             #your CPU to mutiny.
sailors = 20 #How many port workers per active captain.
#time in milliseconds between scans
deluge = 0
flood = 100
medium = 300
slow = 800
trickle = 3000
#Staggering in percent of the speed
none = 0
natural = .1
standard = .25
sloppy = .50
drunken = .75
#Named ports! This is the top 20, but it will name any that are added and identified.
namedport = {
    "21":"FTP",
    "22":"SSH",
    "23":"Telnet",
    "25":"SMTP",
    "53":"DNS",
    "80":"HTTP",
    "110":"POP3",
    "111":"RPCBind",
    "135":"MSRPC",
    "139":"NetBIOS-SSN",
    "143":"IMAP",
    "443":"HTTPS",
    "445":"Microsoft-DS",
    "993":"IMAPS",
    "995":"POP3S",
    "1723":"PPTP",
    "3306":"MYSQL",
    "3389":"MS-WBT-SERVER",
    "5900":"VNC",
    "8080":"HTTP-PROXY"
}


#________________________________________________________________
#________________________________________________________________

#IDEAS
#!!!Validate input!!! Especially the target.
#add setting to scan ports in pseudorandom or nonconsecutive order
#launch default packets, payloads & locations
#Seige a machine- when a port on a targeted machine opens or transmits,
#report or attempt to inject payload. Keep a very watchful eye on the
#opponent machine. Cross-ref ssh and sql versions with metasploit vulnerability libraries?
#linux machines have less ttl on their packets than windows
#Windows machines have 128 hops, can correlate just off of ping?
#Locard's Principle
#Event Time Horizon
#INITIALIZATION
exploitDict = {}
target = 'None'
speed = 0
obfuscationStagger = 0
isMultithread = False
obfuscationStagger = 0
inp = []
ipThreadCounter = 0

#______________________________MAIN_____________________________
typechoice = 0
#INPUT SEQUENCE NETWORK
GUI()
print("\n    NETWORK CIDR, SINGLE IP, or DOMAIN NAME.")
target = input("Target: ")
#SPEED
GUI()
print('\n')
print("             SELECT SCAN DELAY")
print(f"    1)........Reckless     ({deluge}ms delay, parallel scans)")
print(f"    2)........Unapologetic ({flood}ms delay)")
print(f"    3)........Standard     ({medium}ms delay)")
print(f"    4)........Cautious     ({slow}ms delay)")
print(f"    5)........Clandestine  ({trickle}ms delay)")
print("\n")
while True:
    print(f"    Choose 1, 2, 3, 4, or 5:")
    speedChoice = input("?>")
    breakout = False
    if speedChoice == "1":
        isMultithread = True
        speed = deluge
        breakout = True
    elif speedChoice == "2":
        speed = flood
        breakout = True
    elif speedChoice == "3":
        speed = medium
        breakout = True
    elif speedChoice == "4":
        speed = slow
        breakout = True
    elif speedChoice == "5":
        speed = trickle
        breakout = True
    else:
        print("Please enter a valid number.")
    if breakout == True:
        break

#STAGGER
GUI()
print('\n')
print("             SELECT PORT SCAN TIME STAGGER")
print(f"    1)........Perfect     (+-{none * 100}% range)")
print(f"    2)........Proper  (+-{natural * 100}% range)")
print(f"    3)........Natural (+-{standard * 100}% range)")
print(f"    4)........Sloppy   (+-{sloppy * 100}% range)")
print(f"    5)........Drunken  (+-{drunken * 100}% range)")
print('\n')
while True:
    print(f"    Choose 1, 2, 3, 4, or 5:")
    stagChoice = input("?>")
    breakout = False
    if stagChoice == "1":
        obfuscationStagger = none
        breakout = True
    elif stagChoice == "2":
        obfuscationStagger = natural
        breakout = True
    elif stagChoice == "3":
        obfuscationStagger = standard
        breakout = True
    elif stagChoice == "4":
        obfuscationStagger = sloppy
        breakout = True
    elif stagChoice == "5":
        obfuscationStagger = drunken
        breakout = True
    else:
        print("Please enter a valid number.")
    if breakout == True:
        break

#PORTS
GUI()
print("\n")
print("             SELECT TARGET PORTS")
print("    [startport-finishport] for range, or [portA portB portC etc...] for specifics, or [t20] for top 20 ports.")
print("\n")
print(f"    Choose target ports:")
inpport = input("?>")
inp.append(inpport)

#EXECUTION
GUI()

if "/" not in target:
    destination = socket.gethostbyname(target)
else:
    destination = target
if "/" in destination:
    IPlist = ipaddress.ip_network(destination)
    print("\n    Network Scan Selected.")
    for targIP in IPlist.hosts():
        ipThread = threading.Thread(target=testIP, kwargs={'targIP':str(targIP)})
        ipThread.start()
        ipThreadCounter += 1
        if ipThreadCounter % captains == 0:
            ipThread.join()
    ipThread.join()
else:
    print("\n    Single IP Scan Selected.")
    targIP = destination
    testIP(targIP)
#RESULTS
print("\n\n\n    ________RESULTS________")
print("    _______________________")
for machine in exploitDict:
    print(str(machine) + str(exploitDict[machine]))