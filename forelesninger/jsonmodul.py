import json

def les_json(filnavn):
    try:
        with open(filnavn) as fil:
            dict_fra_fil = json.load(fil)
    except FileNotFoundError:
        print("Fant ikke filen.")
        
    else:
        return dict_fra_fil

def skriv_json(dictionary, filnavn):
# Open the file in write mode and pass the
    with open(filnavn, 'w') as file:
        json.dump(dictionary, file, indent=4)