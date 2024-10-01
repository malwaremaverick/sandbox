brettspill = ["Ubongu", "Pandemic", "Ludo", "Monopol", "Mysterium", "Risk", "Pandemic Legacy: Season 1", "Pandemic Season 2" ]

print(brettspill[4:7])

print(brettspill[:2])
print(brettspill[2:])

for spill in brettspill[-3:]:
    print(spill)
    
brettspill.sort()
print(brettspill)
tre_første_spill = brettspill[:3]
print(tre_første_spill)

print(brettspill[::2])

tekst = brettspill[-3]
print(tekst)

print(brettspill[7:13])

print(tekst[-1])
print(tekst[-8:])