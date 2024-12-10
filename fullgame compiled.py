import time
import os
from pathlib import Path
import playsound

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

def start_game():
    clear_screen()
    print("🎵 Skibidi dop dop dop yes yes! 🎵")
    time.sleep(2)
    print("Du vaknar efter det långa fallet...")
    time.sleep(4)
    print("Du känner att du ligger på något ganska mjukt.")
    time.sleep(4)
    print("Efter att du tittat vad du landat på märker du att det är en bädd av gyllene blommor.")
    time.sleep(3)
    print("Tryck [Enter] för att ställa dig upp.")
    input()
    print("Efter att du ställer dig upp hör du en röst.")
    time.sleep(3)
    print("???: Du har rest långt för att komma ända hit.")
    time.sleep(3)
    print("Du vänder dig om för att se något eller någon...")
    time.sleep(3)
    print("???: Jag är inte på ett ställe som du kan se.")
    time.sleep(3)
    print("???: Vad är ditt namn?")
    name = input()
    print(f"Jag tror inte att {name} är ditt namn.")
    time.sleep(3)

    truename = Path.home().name
    print(f"???: Det är inte det, eller hur {truename}?")
    time.sleep(4)
    print(f"???: Så nu, {truename}, ska vi fortsätta?")
    time.sleep(3)

    print('''
Du ser att du är i ett avlångt rum.
Du står fortfarande på blommorna.
Du ser även en utsmyckad öppning i slutet av tunneln.
''')
    time.sleep(3)

    print("Vart ska du nu? [framåt/bakåt]")
    room_1 = input().lower().strip()

    if room_1 == "framåt":
        print("Du går framåt mot öppningen...")
        time.sleep(2)
        corridor_scene()
    elif room_1 == "bakåt":
        print("Du ser en vägg bakom dig. Det finns inget att göra här.")
    else:
        print("Huh? Jag förstod inte det där.")
    input("Tryck [Enter] för att återgå till menyn...")

def corridor_scene():
    clear_screen()
    print("Du går in i rummet och det verkar vara en tom korridor...")
    time.sleep(2)
    print("Du ser vad som ser ut som en liten gul blomma i mitten av korridoren.")
    try:
        playsound.playsound('Undertale OST_ 001 - Once Upon A Time.mp3', block=False)
    except:
        print("Musiken kunde inte spelas upp.")
    print("Blomman?: Hejsan, dig har jag inte sett förut.")
    time.sleep(3)
    print("Blomman vänder sig om och du ser ett ansikte i blommans mitt.")
    time.sleep(3)
    print("Blomman?: Se inte så förvånad ut, har du aldrig sett en blomma förut?")
    time.sleep(3)
    print("Flowey: Jag heter Flowey, blomman Flowey, och jag bor här.")
    time.sleep(3)
    print("Flowey: Vad heter du?")
    floweyanswer = input()
    print(f"Flowey: Men hej på dig {floweyanswer}! Ska jag lära dig hur saker går till här?")
    tutorial = input()
    if tutorial.lower() in ["ja", "y", "yes"]:
        print("Flowey: Perfekt, ska vi börja då.")
    else:
        print("Too bad, du får en tutorial ändå.")

    print("Flowey: Först får du plocka upp ett vapen.")
    time.sleep(2)
    print("Du plockade upp en plastkniv.")
    time.sleep(2)
    print("Flowey: Jag kommer kasta pellets på dig. Du ska undvika dem.")
    time.sleep(3)

    print("Flowey: Du är nu redo för den här världen.")
    time.sleep(2)
    print("Flowey: Kom ihåg: i den här världen är det döda eller bli dödad.")
    time.sleep(3)
    print("Du står i korridoren, och en öppning finns bredvid dig.")
    time.sleep(2)
    print("Du går genom öppningen...")
    input("Tryck [Enter] för att fortsätta till nästa del...")

while True:
    show_menu()
    choice = input("Välj ett alternativ (1 eller 2): ").strip()

    if choice == '1':
        start_game()
    elif choice == '2':
        clear_screen()
        print("Spelet avslutas. Tack för att du tittade förbi!")
        time.sleep(1)
        exit()
    else:
        print("Ogiltigt val. Försök igen.")
        time.sleep(1)
