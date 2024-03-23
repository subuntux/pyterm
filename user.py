#!/usr/bin/env python3

import sqlite3
import hashlib
import time
import subprocess

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('/data/data/com.termux/files/usr/shared/pyterm/db/user.db')
c = conn.cursor()

def check_user_exists():
    c.execute("SELECT * FROM users")
    if c.fetchone():
        return True
    else:
        return False

def register_user():
    username = input("Username: ")
    password = input("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    current_time = int(time.time())
    c.execute("INSERT INTO users (username, password, last_login) VALUES (?, ?, ?)", (username, hashed_password, current_time))
    conn.commit()
    print("Registration successful!")
    # Automatisch anmelden nach der Registrierung
    login_user()

def login_user():
    username = input("Username: ")
    password = input("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = c.fetchone()
    if user:
        current_time = int(time.time())
        c.execute("UPDATE users SET last_login = ? WHERE username = ?", (current_time, username))
        conn.commit()
        print("Login successful!")
        # Python-Datei ausführen
        subprocess.run(["python3", "/data/data/com.termux/files/usr/shared/pyterm/main.py"])
    else:
        print("Incorrect username or password.")

def main():
    if not check_user_exists():
        print("No user found. Please register.")
        register_user()
    else:
        login_user()

    conn.close()

if __name__ == "__main__":
    main()