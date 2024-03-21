#!/usr/bin/env python3

import subprocess
import os

banner = """ 

 _________  _______   ________  _____ ______      
|\___   ___\\  ___ \ |\   __  \|\   _ \  _   \    
\|___ \  \_\ \   __/|\ \  \|\  \ \  \\\__\ \  \   
     \ \  \ \ \  \_|/_\ \   _  _\ \  \\|__| \  \  
      \ \  \ \ \  \_|\ \ \  \\  \\ \  \    \ \  \ 
       \ \__\ \ \_______\ \__\\ _\\ \__\    \ \__\
        \|__|  \|_______|\|__|\|__|\|__|     \|__|
[Term Master.py, (c) by subuntux]
[v.1.0]
"""

def main_menu():
    subprocess.run(["clear"])
    print(banner)
    print("Select an Option")
    print("[1]-Setup")
    print("[2]-Termux Menu")
    print("[3]-X11 Menu")
    print("[4]-API Menu")
    print("[0]-Exit")
    
def get_choice():
    choice = input("select-| ")
    return choice
    
def setup():
    print("")
    print("[*] Start Setup")
    print("[*] Set Wake Lock")
    print("")
    subprocess.run(["termux-wake-lock"])
    print("")
    print("[*] Start Base Installation")
    print("[*] Following Pakages Will Install")
    print("1: nodejs")
    print("2: neovim")
    print("3: git")
    print("4: proot-distro")
    print("5: zshell")
    print("6: wget")
        
    choice = input("Is that ok? (y/n) ").lower()
        
    if choice == 'y':
        print("")
        print("[*] Install Pakages")
        print("[*] Install nodejs")
        print("")
        subprocess.run(["pkg", "install", "nodejs", "-y"])
        print("")
        print("[*] Succesfull")
        print("[*] Install neovim")
        print("")
        subprocess.run(["pkg", "install", "neovim", "-y"])
        print("")
        print("[*] Succesfull")
        print("[*] Install git")
        print("")
        subprocess.run(["pkg", "install", "git", "gh", "-y"])
        print("")
        print("[*] Succesfull")
        print("[*] Install proot-distro")
        print("")
        subprocess.run(["pkg", "install", "proot-distro", "-y"])
        print("[*] Succesfull")
        print("[*] Install zshell")
        print("")
        subprocess.run(["pkg", "install", "zsh", "-y"])
        print("")
        print("[*] Succesfull")
        print("[*] Install wget")
        print("")
        subprocess.run(["pkg", "install", "wget", "which", "-y"])
        print("")
        print("[*] Succesfull")
        print("[*] Finish")
        subprocess.run(["termux-wake-unlock"])
    else:
        print("")
        print("[*] Setup Cancelled")
        subprocess.run(["termux-wake-unlock"])
        
def termux_menu():
    while True:
        subprocess.run("clear")
        print(banner)
        print("Termux Menu")
        print("[1]-Create Cache")
        print("[2]-Backup Termux")
        print("[3]-Restore Backup")
        print("[4]-Set Login")
        print("[5]-Change Repo")
        print("[6]-Setup Storage")
        print("[7]-Update")
        print("[8]-Use adb")
        print("[0]-Exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            print("")
            print("[*] Create Cache")
            os.chdir(os.getenv("HOME"))
            subprocess.run(["mkdir", ".cache"])
            print("[*] Chache Created")
            print("")
        elif choice == '2':
            subprocess.run(["termux-wake-lock"])
            print("")
            print("[*] Start Backup (This can take a while)")
            print("")
            subprocess.run(["termux-backup", "backup.tar.xz"])
            subprocess.run(["mv", "backup.tar.xz", ".cache"])
            print("")
            print("[*] Backup Succesfull")
            print("")
            subprocess.run(["termux-wake-unlock"])
        elif choice == '3':
            subprocess.run(["termux-wake-lock"])
            print("")
            print("[*] Restore Backup (This can take a while)")
            print("")
            os.chdir(os.getenv("HOME"))
            subprocess.run(["cp", ".cache/backup.tar.xz", "."])
            subprocess.run(["termux-restore", "backup.tar.xz"])
            print("")
            print("[*] Restore Succesfull")
            print("")
            subprocess.run(["termux-wake-unlock"])
        elif choice == '4':
            print("")
            print("[*] Set User Login")
            print("")
            os.chdir(os.getenv("HOME"))
            subprocess.run(["wget", "https://raw.githubusercontent.com/MrAlpha786/termux-login-password/master/setup"])
            subprocess.run(["chmod", "+x", "setup"])
            subprocess.run(["bash", "setup"])
            print("")
            print("[*] Succesfull set login")
            print("")
        elif choice == '5':
            subprocess.run(["termux-change-repo"])
        elif choice == '6':
            subprocess.run(["termux-setup-storage"])
        elif choice == '7':
            subprocess.run(["pkg", "update", "-y"])
            subprocess.run(["pkg", "upgrade", "-y"])
        elif choice == '8':
            adb_shell()
        else:
            print("Invalid Option")
        
def x11_menu():
    while True:
        subprocess.run("clear")
        print(banner)
        print("X11 Menu")
        print("[1]-Install X11 Repo")
        print("[2]-Install GUI (low)")
        print("[3]-Install GUI (full)")
        print("[4]-Install X11 Nightly")
        print("[5]-Install VNC")
        print("[6]-Install VNC Viewer")
        print("[7]-Install X11 APK")
        print("[0]-Exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        if choice == '1':
            print("")
            print("[*] Install X11 Repo")
            print("")
            subprocess.run(["pkg", "install", "x11-repo"])
            print("")
            print("[*] Succesfull")
            print("")
        elif choice == '2':
            subprocess.run(["termux-wake-lock"])
            print("")
            print("[*] Install GUI (low)")
            print("")
            subprocess.run(["pkg", "install", "xfce4", "-y"])
            print("")
            print("[*] Succesfull")
            print("")
            subprocess.run(["termux-wake-unlock"])
        elif choice == '3':
            subprocess.run(["termux-wake-lock"])
            print("")
            print("[*] Install GUI (Full)")
            print("")
            subprocess.run(["pkg", "install", "xfce4", "-y"])
            subprocess.run(["pkg", "install", "xfce4-terminal", "-y"])
            subprocess.run(["pkg", "install", "firefox", "-y"])
            print("")
            print("[*] Succesfull")
            print("")
            subprocess.run(["termux-wake-unlock"])
        elif choice == '4':
            print("")
            print("Install X11 Nightly")
            print("")
            subprocess.run(["pkg", "install", "termux-x11-nightly", "-y"])
            print("")
            print("[*] Succesfull")
            print("")
        elif choice == '5':
            print("")
            print("[*] Install VNC")
            print("")
            subprocess.run(["pkg", "install", "tigervnc", "-y"])
            print("")
            print("[*] Succesfull")
            print("")
        elif choice == '6':
            print("")
            print("[*] Load Content")
            subprocess.run(["termux-open-url", "https://play.google.com/store/apps/details?id=com.realvnc.viewer.android"])
            print("[*] Connected")
        elif choice == '7':
            print("")
            print("[*] Load Content")
            subprocess.run(["termux-open-url", "https://github.com/termux/termux-x11/actions/workflows/debug_build.yml"])
            print("[*] Connected")
        else:
            print("Invalid Option")
            
def api_menu():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("API Menu")
        print("[1]-Install API APK")
        print("[2]-Install API Plugin")
        print("[0]-Exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            print("")
            print("[*] Load Content")
            subprocess.run(["termux-open-url", "https://github.com/termux/termux-api/actions/workflows/debug_build.yml"])
            print("[*] Connected")
        elif choice == '2':
            print("")
            print("[*] Install API Plugin")
            print("")
            subprocess.run(["pkg", "install", "termux-api", "-y"])
        else:
            print("Invalid Option")
            
def adb_shell():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("ADB Menu (Shizuku needed)")
        print("[1]-Create Cache")
        print("[2]-Use Existing rish")
        print("[3]-Download Rish")
        print("[0]-Exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            os.chdir(os.getenv("HOME"))
            subprocess.run(["mkdir", ".cache/adb"])
        elif choice == '2':
            subprocess.run(["bash", "/data/data/com.termux/files/usr/shared/pyterm/exist.sh"])
        elif choice == '3':
            subprocess.run(["bash", "/data/data/com.termux/files/usr/shared/pyterm/dl.sh"])
        else:
            print("Invalid Option")
            
while True:
    main_menu()
    choice = get_choice()
    
    if choice == '0':
        break
    elif choice == '1':
        setup()
    elif choice == '2':
        termux_menu()
    elif choice == '3':
        x11_menu()
    elif choice == '4':
        api_menu()
    else:
        print("Invalid Option")