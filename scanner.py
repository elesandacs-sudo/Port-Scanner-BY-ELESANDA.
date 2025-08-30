#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Port Scanner BY ELESANDA

import socket
import threading

# ──────────────── BANNER ──────────────── #
BANNER = r"""
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                BY ELESANDA
"""
print(BANNER)

# ──────────────── SCANNER ──────────────── #

open_ports = []

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)   # hızlı tarama
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} OPEN")
            open_ports.append(port)
        sock.close()
    except:
        pass

def run_scanner(target):
    print(f"\n[*] Scanning target: {target}\n")
    threads = []
    for port in range(1, 65536):   # full tarama
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("\nScan Completed.")
    if open_ports:
        print("Open Ports:", open_ports)
    else:
        print("No open ports found.")

# ──────────────── MAIN ──────────────── #

if __name__ == "__main__":
    target_ip = input("Enter Target IP: ")
    run_scanner(target_ip)
