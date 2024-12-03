import time
from pathlib import Path


#story börjar
print("du vaknar efter det långa fallet")
time.sleep(4)
print("du känner at du ligger på något ganska mjukt")
time.sleep(4)
print("efter att du tittat vad du landat på märker du att det är en bed av gylene blommor")
time.sleep(6)
print("tryck [enter] för att ställa dig up")
input()
print("efter att du ställer dig up hör du en röst")
time.sleep(4)
print("???: du har rest långt för att komma ända hit")
time.sleep(4)
print("du vänder dig om för att se vem som se något eller någon")
time.sleep(4)
print("???: jag är inte på ett ställe som du kan se.")
time.sleep(4)
print("???: vad är ditt namn?")
name = input()
print(f"jag tror inte att {name} är ditt namn")
time.sleep(4)
#namn check
truename =  Path.home().name
print(f"???: det är inte det eller hur {truename}?")
time.sleep(6)
print(f"???: så nu {truename} ska vi fortsätta?")
time.sleep(3)
print('''du ser att du är i ett avlångt rum
      du står fortfarande på blommorna
      du ser även en utsmyckad öppning i slutet av tunneln''')
time.sleep(12)
#frågar vart du ska
print("vart ska du nu?")
room_1 = input()
if room_1.lower == "framåt":
    pass
elif room_1.lower == "bakåt":
    print("du ser en vägg")
else:
    print("huh?")




