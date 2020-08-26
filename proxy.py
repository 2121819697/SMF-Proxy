# -*- coding: utf-8 -*-
import socket
import time
import argparse
import sys
import os
import platform

colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    end = red = white = green = yellow = run = bad = good = info = que = ''
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'
    back = '\033[7;91m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'
logo =f"""
{yellow}
 _____  _____   ______   ____     __
|  __ \|  __ \ / __ \ \ / /\ \   / /
| |__) | |__) | |  | \ V /  \ \_/ / 
|  ___/|  _  /| |  | |> <    \   /  
| |    | | \ \| |__| / . \    | |   
|_|    |_|  \_\\____/_/ \_\   |_|   
                                    
                                    
{end}
{yellow}

usage:{end} proxy.py [-h] [-t TIMEOUT] [-i PROXY_IP] [-p PORT]

{yellow}optional arguments{end}:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        timeout
  -i PROXY_IP, --IP PROXY_IP
                        Proxy IP
  -p PORT, --port PORT  Proxy Port
{red}Version:1.7{end}
{green}By:@SMDD{end}
"""
port ="8080"
timeout_ = 10
host =""
addr_ = (""+str(host),int(port))
def main():
    print(logo)
    global host
    global timeout_
    global port
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--timeout', help='timeout',
                        dest='Timeout', type=int)
    parser.add_argument('-i','--IP', help='Proxy IP',
                        dest='Proxy_IP', type=str)
    parser.add_argument('-p','--port', help='Proxy Port',
                        dest='Port', type=int)
    args = parser.parse_args()
    host = args.Proxy_IP
    timeout_ = args.Timeout
    port = args.Port
    proxy()
def proxy():
    global addr_
    global timeout_
    try:
        server = socket.socket()
        server.settimeout(timeout_)
        server.bind((addr_))
        server.listen(10)
        conn, addr = server.accept()
        data = conn.recv(9086).decode("utf-8","ignore")
        server.close()
        conn.close()
        print(f"[{green}INFO{end}]Host:"+str(addr))
        print(f"[{yellow}***{end}]Info:")
        print(data)
        proxy()
    except:
        print(f"{bad}Error")
main()
