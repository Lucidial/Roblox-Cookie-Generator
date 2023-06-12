import random
from colorama import Fore, Style

logo = f'''
{Fore.MAGENTA}
███████╗██╗   ██╗███╗   ██╗███████╗ █████╗ ██╗██╗     
██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝██╔══██╗██║██║     
███████╗ ╚████╔╝ ██╔██╗ ██║█████╗  ███████║██║██║     
╚════██║  ╚██╔╝  ██║╚██╗██║██╔══╝  ██╔══██║██║██║     
███████║   ██║   ██║ ╚████║██║     ██║  ██║██║███████╗
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝
{Fore.CYAN}1.12A{Style.RESET_ALL}
'''

def generate_cookie():
    cookie_string = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(712))
    return cookie_string

def main():
    print('\033c')  # Clear console
    print(logo)
    num_cookies = int(input(f"{Fore.RED}How many cookies would you like to generate? {Style.RESET_ALL}"))

    cookies = []
    for _ in range(num_cookies):
        cookies.append(generate_cookie())

    print('\n'.join(cookies))

if __name__ == '__main__':
    main()
