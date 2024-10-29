import json

planeter = [
    {'navn': 'Merkur', 'tyngdekraft': 3.7},
    {'navn': 'Venus', 'tyngdekraft': 8.87},
    {'navn': 'Jorden', 'tyngdekraft': 9.807},
    {'navn': 'Mars', 'tyngdekraft': 3.721},
    {'navn': 'Jupiter', 'tyngdekraft': 24.79},
    {'navn': 'Saturn', 'tyngdekraft': 10.44},
    {'navn': 'Uranus', 'tyngdekraft': 11.15}
]

filnavn = "planeter.json"

with open(filnavn, "w") as utfil:
    json.dump(planeter, utfil, indent=4)
    
    
with open(filnavn, "r") as fil:
    planeter_fra_fil = json.load(fil)
    print(planeter_fra_fil)
    print(type(planeter_fra_fil))
    
json_string = '{"dyr": "katt", "navn": "Astaroth", "alder": 100}'
print(type(json_string))

katt = json.loads(json_string)
print(katt)
print(type(katt))
print(f"Katten {katt['navn']} er {katt['alder']} år gammel.")
