#!/usr/bin/env python3

import sqlite3
import hashlib
import time
import subprocess

MAX_LOGIN_ATTEMPTS = 3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('/data/data/com.termux/files/usr/shared/pyterm/db/user.db')
c = conn.cursor()

def login_user():
    login_attempts = 0
    while login_attempts < MAX_LOGIN_ATTEMPTS:
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
            # Hier können zusätzliche Aktionen für den erfolgreichen Login durchgeführt werden.
            # Beispielsweise:
            # do_something_after_login()
            conn.close()  # Schließen der Datenbankverbindung
            return
        else:
            print("Incorrect username or password.")
            login_attempts += 1

    # Wenn der Benutzer die maximale Anzahl von Anmeldeversuchen erreicht hat
    if login_attempts == MAX_LOGIN_ATTEMPTS:
        print("Maximum login attempts reached.")
        subprocess.run(["termux-wake-lock"])  # Verhindern, dass das Gerät in den Ruhezustand wechselt
        subprocess.run(["termux-wake-unlock"])  # Aufwecken des Geräts (falls es im Ruhezustand ist)
        subprocess.run(["termux-reset"])
        return

def main():
    login_user()

if __name__ == "__main__":
    main()
