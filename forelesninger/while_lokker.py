teller = 10
while teller > 0:
    print(teller)
    teller -= 1

print(f"Nåværende verdi av teller: {teller}")
while teller < 11:
    print(teller)
    teller += 1
    
liste_med_tall = []

for tall in range(7):
    liste_med_tall.append(tall)
print(liste_med_tall)

while 3 in liste_med_tall:
    liste_med_tall.pop()
    print(liste_med_tall)
    
while liste_med_tall:
    liste_med_tall.pop()
    print(liste_med_tall)
    
kjør = True
while kjør:
    print("test")
    for nummer in range(2):
        print(nummer)

    en_gang_til = input("Vil du kjøre en gang til?: (Y/N)")
    kjør = en_gang_til.upper() == "Y"
    