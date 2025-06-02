# Write the main colorful CLI launcher to GeoStalker/geostalker.py
main_cli_code = """"""


import os
import sys
import time
from colorama import init, Fore, Style
from pyfiglet import Figlet
from halo import Halo
from color_utils.printx import print_success, print_error, print_info, ask_input

init(autoreset=True)

def banner():
    f = Figlet(font='slant')
    print(Fore.MAGENTA + f.renderText('GeoStalker'))

def menu():
    print(Fore.CYAN + Style.BRIGHT + "\\n[ MAIN MENU ]")
    print(Fore.YELLOW + "1. Instagram Recon")
    print("2. IP Geolocation")
    print("3. Face Match")
    print("4. Image Geotag Extractor")
    print("5. Email Breach Check")
    print("6. Username Cross-Platform Lookup")
    print("7. Discord/Telegram Recon")
    print("8. Drone Image Recon (Experimental)")
    print("9. Generate Report")
    print("0. Exit\\n")

def run_module(option):
    spinner = Halo(text='Running module...', spinner='dots')
    spinner.start()
    time.sleep(1.5)  # Simulate loading
    spinner.stop()
    print_success(f"Module {option} executed (stub).")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()

    while True:
        menu()
        choice = ask_input("Enter your choice: ")
        if choice == '0':
            print_info("Goodbye, GeoStalker out.")
            break
        elif choice in map(str, range(1, 10)):
            run_module(choice)
        else:
            print_error("Invalid input, try again.")

if __name__ == '__main__':
    main()
