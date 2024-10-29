import random
def skriv_header():
    print("=======================================")
    print("== Hva er din vekt på en annen planet? ==")
    print("=======================================")

def skriv_ut_planetliste(planeter):
    for index, planet in enumerate(planeter, 1):
        print(f"{index} - {planet['navn']}")

def velg_tilfeldig(valgt_samling):
    random_index = random.randrange(0, len(valgt_samling))
    valgt_element = valgt_samling[random_index]
    return valgt_element

def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
    beregnet_vekt = (din_vekt/jordtyngdekraft) * planettyngdekraft
    return round(beregnet_vekt, 2)

def en_gang_til():
    svar = input("Vil du prøve en gang til? (y/n) ")
    return svar.lower() == "y"

planeter = [{'navn' : 'Merkur', 'tyngdekraft':3.7},
            {'navn' : 'Venus', 'tyngdekraft':8.87},
            {'navn' : 'Jorden', 'tyngdekraft':9.807},
            {'navn': 'Mars', 'tyngdekraft': 3.721},
            {'navn': 'Jupiter', 'tyngdekraft': 24.79},
            {'navn': 'Saturn', 'tyngdekraft': 10.44},
            {'navn': 'Uranus', 'tyngdekraft':11.15}
            ]

# ----------------------------

run = True
while run:
    skriv_header()
    skriv_ut_planetliste(planeter)
    try:
        valgt_planet = int(input("Velg en planet ved å skrive et tall: "))
    except ValueError:
        print("Ugyldig valg, prøv igjen!")
        continue

    if valgt_planet == 0:
        valgt_planet = velg_tilfeldig(planeter)
        print(f"Du fikk planeten {valgt_planet['navn']}!")
    else:
        try:
            valgt_planet = planeter[valgt_planet - 1]
            print(f"Du har valgt planeten {valgt_planet['navn']}!")
        except IndexError:
            print("Ugyldig valg, prøv igjen!")
            continue

    try:
        din_vekt = float(input("Hva er din vekt på Jorden? "))
    except ValueError:
        print("Ugyldig tall, prøv igjen!")
        continue
    
    vekt_pa_annen_planet = beregn_vekt(din_vekt, valgt_planet['tyngdekraft'])
    
    print(f"Din vekt på planeten {valgt_planet['navn']} er {vekt_pa_annen_planet:.2f} kg, som har tyngdekraft {valgt_planet['tyngdekraft']:.2f}")

    run = en_gang_til()

