import random

def ounte_kogus():
    poialpoisid = int(input("Sisesta pöialpoiste arv:"))
    tulemus = ""
    kokku = 0
    
    for i in range(1, poialpoisid + 1):
        number = random.randint(1, 2)
        tulemus += str(number) + '\n'
        kokku += number
        
    print("Pöialpoisid saavad:\n" + tulemus,"Lumivalgukesele jäi:", 14 - kokku)

ounte_kogus()
    