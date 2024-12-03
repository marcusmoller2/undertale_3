import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("Välkommen till...")
    time.sleep(2)

    print('''
██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗ ████████╗ █████╗ ██╗     ███████╗    ██████╗ 
██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║     ██╔════╝    ╚════██╗
██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝   ██║   ███████║██║     █████╗       █████╔╝
██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗   ██║   ██╔══██║██║     ██╔══╝       ╚═══██╗
╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗███████╗    ██████╔╝
 ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ 
                                                                                         
    ''')
    time.sleep(2)
    print("1. Börja spelet")
    print("2. Avsluta")
    print()


while True:
    show_menu()
    choice = input("Välj ett alternativ (1 eller 2): ").strip()  
    
    if choice == '1':  
        clear_screen()
        print("🎵 Skibidi dop dop dop yes yes! 🎵")
        time.sleep(2)
        print("Låt äventyret börja!")
        input()
    elif choice == '2':  
        clear_screen()
        print("Spelet avslutas. Tack för att du tittade förbi!")
        time.sleep(1)
        exit()  
    else:  
        print("Ogiltigt val. Försök igen.")
        time.sleep(1)
