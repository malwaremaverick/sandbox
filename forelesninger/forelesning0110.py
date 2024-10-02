import random

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

kjør = True
while kjør:
    print("\n ===================================")
    print(" ==  Hva er din vekt på en annen planet?  ==")
    print(" ===================================")
    
    for planetnummer, planet in enumerate(planeter, 1):
        print(f"{planetnummer} - {planet}")
    print("0 - Tilfeldig planet")

    valgt_planetnummer = input("\n Velg en planet ved å skrive et tall: ")
    try:
        valgt_planetnummer = int(valgt_planetnummer)
    except ValueError:
        print("Ugyldig valg, prøv igjen!")
        continue
    
    if valgt_planetnummer == 0:
        valgt_planetnummer = random.randint(1, len(planeter))
        print(f"Du har fått tilfeldig planet: {planeter[valgt_planetnummer-1]}!")
    elif 1 <= valgt_planetnummer <= len(planeter):
        valgt_planet = planeter[valgt_planetnummer-1]
        print(f"Du har valgt {valgt_planet}! ")
        
        try:
            din_vekt = float(input("Hva er din vekt på Jorden? "))
        except ValueError:
            print("Ugyldig tall, prøv igjen!")
            continue
        
        # Utregninger
        jordens_tyngdekraft = tyngdekraft[2]
        din_masse = din_vekt / jordens_tyngdekraft
        din_vekt_på_planet = round(din_masse * tyngdekraft[valgt_planetnummer-1], 2)
        
        print(f"Din vekt på planeten {valgt_planet} er {din_vekt_på_planet:.2f} kg, som har tyngdekraft {tyngdekraft[valgt_planetnummer-1]:.2f}")
    else:
        print("Ugyldig valg, prøv igjen!")
        

    en_gang_til = input("Vil du prøve igjen? (Y/N) ").upper()
    kjør = en_gang_til == "Y"

