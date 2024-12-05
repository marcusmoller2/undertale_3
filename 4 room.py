import time
def rum():
    print("Du öppnar en dörr och går in i ett mörkt rum.")
    time.sleep(3)
    print("Genom rummet känner du en kall vindpust")
    time.sleep(3)
    print("Du får kalla kårrar")
    time.sleep(3)
    print("Du fortsätter fram i rummet och stötter på fyra dörrar")
    time.sleep(3)
    print("Du kan gå: fram, bak, höger eller vänster.")
    time.sleep(3)
    val = input("Vart vill du gå? ").strip().lower()
    # Använder time.sleep för att sprida texten och låter bli att rensa skärmen för att kunna se tidigare text.
    if val == "fram":
        pass
    elif val == "bak":
        pass
    elif val == "höger":
        pass
    elif val == "vänster":
        pass
    else:
        print("Ogiltigt val. Försök igen.")
        rum()  # Återkallar funktionen för att låta spelaren välja igen.

# Kör funktionen för att testa rummet
rum()
