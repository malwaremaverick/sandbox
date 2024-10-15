import random

brettspill = ["Ubongu", "Pandemic", "Ludo", "Monopol", "Mysterium"]

def velg_tilfeldig_brettspill(spilliste):
    indexnummer = random.randrange(len(spilliste))
    return spilliste.pop(indexnummer)

valgt_brettspill = velg_tilfeldig_brettspill(brettspill[:])

print(f"Du valgte {valgt_brettspill}")
print(brettspill)


    
