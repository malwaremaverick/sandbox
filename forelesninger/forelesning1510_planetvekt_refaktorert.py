def skriv_header():
    print("=======================================")
    print("== Hva er din vekt på en annen planet? ==")
    print("=======================================")

def skriv_ut_planetliste(planeter):
    for index, planet in enumerate(planeter):
        print(f"{index+1} - {planet['navn']}")
3
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
    valgt_planet = int(input("Velg en planet ved å skrive et tall: "))
    if valgt_planet == 0:
        continue
    try:
        din_vekt = float(input("Hva er din vekt på Jorden? "))
    except ValueError:
        continue
    
    jordens_tyngdekraft = planeter[2]['tyngdekraft']
    din_masse = din_vekt / jordens_tyngdekraft
    din_vekt_paa_planet = round(din_masse * planeter[valgt_planet-1]['tyngdekraft'], 2)
    
    print(f"Din vekt paa planeten {planeter[valgt_planet-1]['navn']} er {din_vekt_paa_planet:.2f} kg, som har tyngdekraft {planeter[valgt_planet-1]['tyngdekraft']:.2f}")
    
    run = False


