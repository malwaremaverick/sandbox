brettspill = ["Ubongu", "Pandemic", "Ludo", "Monopol", "Mysterium"]

for spill in brettspill:
    print(f"{spill} er et bra spill!")
    
for bokstav in "Ubongo":
    print(bokstav)
    
#print(brettspill)
#print(brettspill[0])

pandemic_legacy_season = "Pandemic Legacy: Season"

for nummer_i_serien in range(1, 4):
    pandemic_legacy = f"{pandemic_legacy_season} {nummer_i_serien}"
    
    if pandemic_legacy not in brettspill:
        brettspill.append(pandemic_legacy)
        print(f"Legger til {pandemic_legacy} i lista!")
    
print(brettspill)

for spill in brettspill:
    print(spill)
    
brettspill.append("Risk")
brettspill.append("Risk")
brettspill.append("Risk")
print(brettspill)

while "Risk" in brettspill:
    brettspill.remove("Risk")
    print(brettspill)
    

