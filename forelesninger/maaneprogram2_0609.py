print("Hva er din vekt på andre planeter?")

din_vekt = input("Hva er din vekt på jorden? (i hele kg): ")

if din_vekt.isnumeric() == True:
    din_vekt = int(din_vekt)
    print("OK")
    
else:
    print(f"{din_vekt} er ikke et gyldig vekt.")
    exit()
    
if din_vekt <= 0:
    print(f"Din vekt, {din_vekt} er ikke positiv. Prøv igjen!")
    exit()
    
elif din_vekt > 600:
    print(f"{din_vekt} er enten verdensrekord, eller så lyver du!")
    exit()
        
planetnavn = input("Hva er planetens navn?: ")
if planetnavn == "Pluto" or planetnavn == "pluto":
    print("Pluto er ingen planet, men OK")
    
planetens_tyngdekraft = input("Hva er planetens tyngdekraft?: ")
planetens_tyngdekraft = float(planetens_tyngdekraft)

if planetens_tyngdekraft <= 0:
    print(f"Tyngdekraften, {planetens_tyngdekraft}, kan ikke være 0 eller lavere.")
    exit()
    
jordens_tyngdekraft = 9.807

din_masse = din_vekt / jordens_tyngdekraft

din_planetvekt = din_masse * planetens_tyngdekraft
din_planetvekt = round(din_planetvekt, 2)

print(f"Vekten din på planeten {planetnavn}, med tyngdekraft {planetens_tyngdekraft} m/s2, er {din_planetvekt} kg.")