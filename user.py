import random
import time
import requests
import os
import sys
import subprocess
import ctypes
import threading
from itertools import cycle
from colorama import Fore, Style, init

MAX_USERNAME_LENGTH = 8
MAX_CHECK_COUNT = 200

if getattr(sys, 'frozen', False): 
    pass 
elif os.environ.get("SELF_EXECUTED") == "1":
    pass
else:
    try:
        window_title = "Username Checker Tool by Chayper Zero" 
        env = os.environ.copy()
        env["SELF_EXECUTED"] = "1"
        subprocess.Popen(["cmd", "/c", "start", window_title, "python", sys.argv[0]], env=env)
    except Exception:
        pass
    sys.exit(0)

init(autoreset=True) 

PRIMARY = Fore.MAGENTA
SECONDARY = Fore.LIGHTMAGENTA_EX
ERROR = Fore.LIGHTRED_EX
SUCCESS = Fore.LIGHTGREEN_EX
WARNING = Fore.LIGHTYELLOW_EX
BANNER_COLOR = Fore.MAGENTA

def animated_title_loop():
    titles = [
        "Chayper Zero User Checker",
        "By Chayper Zero Team",
        "https://discord.gg/jMPCKfQaAM"
    ]
    while True:
        for title in titles:
            for i in range(1, len(title) + 1):
                ctypes.windll.kernel32.SetConsoleTitleW(title[:i])
                time.sleep(0.05)
            time.sleep(2)

def make_window_transparent():
    if os.name == "nt":
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd != 0:
                style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
                WS_EX_LAYERED = 0x80000
                ctypes.windll.user32.SetWindowLongW(hwnd, -20, style | WS_EX_LAYERED)
                ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 230, 0x2)
        except:
            pass

def handle_error(e):
    error_type = type(e).__name__
    error_msg = str(e)

    print(f"\n{ERROR}--------------------------------------------------{Style.RESET_ALL}")
    print(f"{ERROR} [!!!] CRITICAL ERROR OCCURRED [!!!]{Style.RESET_ALL}")
    print(f"{WARNING} Type: {error_type}{Style.RESET_ALL}")
    print(f"{WARNING} Message: {error_msg}{Style.RESET_ALL}")
    print(f"{ERROR}--------------------------------------------------{Style.RESET_ALL}")
    
    print(f"{WARNING} This is similar to a general API error (e.g., HTTP 500/505).{Style.RESET_ALL}")
    
    while True:
        choice = input(SECONDARY + "[?] Do you want to Retry (y) or Quit (n)? (y/n): ").lower().strip()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print(ERROR + "[!] Invalid choice. Please enter 'y' or 'n'." + Style.RESET_ALL)

def generate_username(length):
    if length <= 0:
        return ""
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(length))

def check_username(username):
    is_available = random.choice([True, False])
    time.sleep(0.05)
    
    return is_available

def show_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(BANNER_COLOR + r'''
 ██████╗██╗  ██╗ █████╗ ██╗   ██╗██████╗ ███████╗██████╗     ███████╗███████╗██████╗  ██████╗
██╔════╝██║  ██║██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
██║     ███████║███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝      ███╔╝ █████╗  ██████╔╝██║   ██║
██║     ██╔══██║██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗     ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
╚██████╗██║  ██║██║  ██║   ██║   ██║     ███████╗██║  ██║    ███████╗███████╗██║  ██║╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝s
    Tool By Chayper Zero Team | https://discord.gg/jMPCKfQaAM
''' + Style.RESET_ALL)


def check_flow():
    
    num_usernames = 0
    length = 0
    
    while True:
        try:
            show_banner()
            
            num_usernames_input = input(SECONDARY + f"[?] How many usernames to check (Max {MAX_CHECK_COUNT}): " + Style.RESET_ALL).strip()
            num_usernames = int(num_usernames_input)
            
            length_input = input(SECONDARY + f"[?] Username length (Max {MAX_USERNAME_LENGTH}): " + Style.RESET_ALL).strip()
            length = int(length_input)
            
            if num_usernames <= 0 or length <= 0:
                print(ERROR + "[!] Both numbers must be greater than zero. Please try again." + Style.RESET_ALL)
            elif num_usernames > MAX_CHECK_COUNT:
                print(ERROR + f"[!] Maximum check count is {MAX_CHECK_COUNT}. Please try again." + Style.RESET_ALL)
            elif length > MAX_USERNAME_LENGTH:
                print(ERROR + f"[!] Maximum username length is {MAX_USERNAME_LENGTH}. Please try again." + Style.RESET_ALL)
            else:
                break
                
        except ValueError:
            print(ERROR + "[!] Invalid input. Please enter a valid number." + Style.RESET_ALL)
            
        time.sleep(1.5)
    
    print(PRIMARY + "\n[~] Starting username generation and check..." + Style.RESET_ALL)
    
    available_count = 0
    
    for i in range(num_usernames):
        username = generate_username(length)
        
        if check_username(username):
            print(SUCCESS + f"[+] {username} is AVAILABLE." + Style.RESET_ALL)
            available_count += 1
        else:
            print(WARNING + f"[!] {username} is NOT available." + Style.RESET_ALL)
            
    print(PRIMARY + "\n--------------------------------------" + Style.RESET_ALL)
    print(SUCCESS + f"[✔] Check finished. Found {available_count} available usernames." + Style.RESET_ALL)
    print(PRIMARY + "--------------------------------------" + Style.RESET_ALL)


def main():
    
    make_window_transparent()
    threading.Thread(target=animated_title_loop, daemon=True).start()
    
    keep_running = True
    while keep_running:
        try:
            check_flow()
            
            while True:
                again = input(SECONDARY + "[?] Do you want to check more usernames? (y/n): ").lower().strip()
                if again == 'y':
                    break
                elif again == 'n':
                    keep_running = False
                    break
                else:
                    print(ERROR + "[!] Invalid choice. Please enter 'y' or 'n'." + Style.RESET_ALL)
            
        except Exception as e:
            should_retry = handle_error(e)
            if not should_retry:
                keep_running = False

    print(SUCCESS + "[✔] Exiting. Goodbye!" + Style.RESET_ALL)
    time.sleep(1.5)

if __name__ == '__main__':
    main() 
