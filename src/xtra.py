#!/usr/bin/env python3

import subprocess
import os 

banner = """ 
   ___       __              
  / _ \__ __/ /____ ______ _ 
 / ___/ // / __/ -_) __/  ' \
/_/   \_, /\__/\__/_/ /_/_/_/
     /___/                   
[Term Master.py, (c) by subuntux]
[v.1.3]
"""


def main_menu():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("[1]-| proot-distro menu")
        print("[2]-| termux-package-helper")
        print("[3]-| create-repository")
        print("[4]-| add external repositorys")
        print("[5]-| termux-browser")
        print("[0]-| exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            proot_menu()
        elif choice == '2':
            pkg_helper()
        elif choice == '3':
            create_repo()
        elif choice == '4':
            add_repo()
        elif choice == '5':
            browser()
        else:
            print("Invalid Option")
            
def proot_menu():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("[1]-| install distro")
        print("[2]-| login distro")
        print("[3]-| delete distro")
        print("[0]-| exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            install_distro()
        elif choice == '2':
            login_distro()
        elif choice == '3':
            delete_delete()
        else:
            print("[!]-| Invalid Option !!!")
            
def pkg_helper():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("[1]-| setup")
        print("[2]-| create meta data")
        print("[3]-| create package")
        print("[0]-| exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            print("[*]-| wake lock")
            subprocess.run(["termux-wake-lock"])
            print("[*]-| install proot-distro and termux-create-package")
            print("")
            subprocess.run(["pkg", "install", "proot-distro", "termux-create-package", "-y"])
            print("")
            print("[*]-| succesful")
            print("[*]-| wake unlock)
            subprocess.run(["termux-wake-unlock"])
        elif choice == '2':
            subprocess.run(["bash", "/data/data/com.termux/files/usr/shared/pyterm/meta.sh"])
        elif choice == '3':
            subprocess.run(["termux-create-package", "*.deb"])
        else:
            print("[!]-| Invalid Option !!!")
            
def create_repo():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("[1]-| setup")
        print("[2]-| create apt-repo")
        print("[0]-| exit")
        
        choice = input("select-| ").lower()
        
        if choice == '0':
            break
        elif choice == '1':
            subprocess.run(["pkg", "termux-apt-repo", "-y"])
        elif choice == '2':
            
            in_fold = input("input-| ")
            out_fold = input("output-| ")
            print("[*]-| Select input/output folder")
            print("[*]-| go from home dir")
            subprocess.run(["termux-apt-repo", in_fold, out_fold])
            print("[*]-| repo created")
        else:
            print("[!]-| Invalid Option !!!")
            
def add_repo():
    while True:
        subprocess.run(["clear"])
        print(banner)
        print("[1]-| first setup")
        print("[2]-| add repo")
        print("[0]-| exit")
        
        repo_url = input("repo-url-| ")
        list_name = input("name-| ")
        
        choice = input("select-| ").lower()
        
        base = "/data/data/com.termux/files/etc/apt/sources.list.d/"
        
        path = f"{base}/{list_name}.list"
        
        if choice == '0':
            break
        elif choice == '1':
            subprocess.run(["mkdir", "-p", base])
        elif choice == '2':
            with open(path, "a") as file:
                file.write(repo_url + "\n")
        else:
            print("[!]-| Invalid Option !!!")
            
def browser():
    subprocess.run(["python3", "/data/data/com.termux/files/usr/shared/pyterm/browser.py"])
    
def install_distro():
    while True:
        distro = input("distro-| ")
        subprocess.run(["pd", "i", distro])
        
def login_distro():
    while True:
        distro = input("distro-| ")
        subprocess.run(["pd", "sh", distro])
        
def delete_delete():
    while True:
        distro = input("distro-| ")
        subprocess.run(["pd", "rm", distro])