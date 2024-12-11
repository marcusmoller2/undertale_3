import random
inventory = "stick, health potion"
helditem = "toyknife"
armor = "bandage"
def contains_health_potion(inventory_string):
    items = inventory_string.split(", ")
    return "health potion" in items and len(items) > 1
def combat(enemytype):
    if helditem == "kniv":
        self_attack = 10
    elif helditem == "spjut":
        self_attack = 12
    elif helditem == "yxa":
        self_attack = 15
    elif helditem == "svärd":
        self_attack = 18
    elif helditem == "väldigt stor sked":
        self_attack = 45
    if armor == "bandage":
        self_defense = 15
    elif armor == "poncho":
        self_defense = 25
    elif armor == "fresh j's":
        self_defense = 35
    elif armor == "rustning":
        self_defense = 45
    elif armor == "aura":
        self_defense = 100
    if enemytype == "flowey":
        health = 30
        damage = 2
        mercy = 4
        print("flowey attacks")
    while self_defense or health > 0:
        print ("[attack] [act] [item] [mercy]")
        turn = input()
        if turn.lower == "attack":
            accuracy = random.randint(1, 100)
            if accuracy > 20:
                health = health - self_attack
        elif turn.lower == "act":
            print ("[check] [talk] ")
            act = input()
            if act.lower == "check":
                print(health)
                print(damage)
            elif act.lower == "talk":
                print(f"du pratar med {enemytype}")
                mercy = mercy - 1
        elif turn.lower == "item":
            print(inventory)
            item = input()
            if item.lower == "health potion":
                if contains_health_potion(inventory) == True:
                    print("du använde den")
                    self_defense = self_defense + 10
                    substring_to_remove = "health potion, "
                    inventory = inventory.replace(substring_to_remove, "")

            
            