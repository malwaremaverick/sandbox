brettspill = {'tittel': 'dixit',
              'spilletid': 30,
              'aldersgrense': 8}

for key in brettspill.keys():
    print(key, brettspill[key])
    
for value in brettspill.values():
    print(value)
    
for key, value in brettspill.items():
    print(f"{key} - {value}")

for key in brettspill.items():
    print(key)