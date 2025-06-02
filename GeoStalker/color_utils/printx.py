from colorama import Fore, Style

def print_success(text):
    print(Fore.GREEN + Style.BRIGHT + "[✔] " + text + Style.RESET_ALL)

def print_error(text):
    print(Fore.RED + Style.BRIGHT + "[✖] " + text + Style.RESET_ALL)

def print_info(text):
    print(Fore.CYAN + Style.BRIGHT + "[i] " + text + Style.RESET_ALL)

def print_warning(text):
    print(Fore.YELLOW + Style.BRIGHT + "[!] " + text + Style.RESET_ALL)

def ask_input(prompt):
    return input(Fore.MAGENTA + Style.BRIGHT + prompt + Style.RESET_ALL)
