from colorama import init, Fore, Style
init(autoreset=True)

# ------------ Setup ------------

def setup():
    # Create appdata folder
    import os
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager"):
        os.makedirs(os.environ['APPDATA'] + "\\RemoteManager")
    # Create logs folder
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager\\logs"):
        os.makedirs(os.environ['APPDATA'] + "\\RemoteManager\\logs")
    # Create config folder
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager\\config"):
        os.makedirs(os.environ['APPDATA'] + "\\RemoteManager\\config")
    # Create config file
    if not os.path.exists(os.environ['APPDATA'] + "\\RemoteManager\\config\\config.json"):
        with open(os.environ['APPDATA'] + "\\RemoteManager\\config\\config.json", "w") as f:
            f.write("{}")

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
    print(Fore.WHITE + "RemoteManager v1.0 - By Gerrxt - https://github.com/Gerrxt07/RemoteManager")
    setup()

# ------------ Run ------------

if __name__ == "__main__":
    main()