from colorama import init, Fore, Style
import os
import datetime
import time
init(autoreset=True)


# ------------ Logging ------------

current_log_file = None

def get_log_filename():
    global current_log_file
    if current_log_file is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_dir = os.path.join(os.environ['APPDATA'], "RemoteManager", "logs")
        current_log_file = os.path.join(log_dir, f"log_{timestamp}.txt")
    return current_log_file

def log(message, level, log_file):
    timestamp = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
    if level == "info":
        print(Fore.GREEN + f"[{timestamp} - Info] " + message)
        if log_file:
            with open(get_log_filename(), "a") as f:
                f.write(f"{timestamp} - [Info] - {message}\n")
    elif level == "warn":
        print(Fore.YELLOW + f"[{timestamp} - Warnung] " + message)
        if log_file:
            with open(get_log_filename(), "a") as f:
                f.write(f"{timestamp} - [Warnung] - {message}\n")
    elif level == "error":
        print(Fore.RED + f"[{timestamp} - Error] " + message)
        if log_file:
            with open(get_log_filename(), "a") as f:
                f.write(f"{timestamp} - [Error] - {message}\n")

# ------------ Setup ------------

def setup():
    # Erstelle AppData Ordner
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager"):
        os.makedirs(os.environ['APPDATA'] + "\\RemoteManager")
        log("AppData Ordner erstellt", "info", False)
    # Erstelle Logs Ordner
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager\\logs"):
        os.makedirs(os.environ['APPDATA'] + "\\RemoteManager\\logs")
        log("Logs Ordner erstellt", "info", False)
    # Erstelle Config Ordner
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager\\config"):
        os.makedirs(os.environ['APPDATA'] + "\\RemoteManager\\config")
        log("Config Ordner erstellt", "info", False)
    # Erstelle Config Datei
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager\\config\\config.json"):
        with open(os.environ['APPDATA'] + "\\RemoteManager\\config\\config.json", "w") as f:
            f.write("{}")
        log("Config Datei erstellt", "info", False)

# ------------ Main ------------

def main():
    logo = r"""
 ____                      _         __  __                                   
|  _ \ ___ _ __ ___   ___ | |_ ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| |_) / _ \ '_ ` _ \ / _ \| __/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
|  _ <  __/ | | | | | (_) | ||  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   
|_| \_\___|_| |_| |_|\___/ \__\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                              |___/           
    """
    print(Fore.CYAN + logo)
    print(Fore.CYAN + "RemoteManager v1.0 - By Gerrxt - https://github.com/Gerrxt07/RemoteManager")
    setup()
    log("Programm gestartet", "info", True)
    time.sleep(5)
    log("Programm gestoppt", "warn", True)

# ------------ Run ------------

if __name__ == "__main__":
    main()