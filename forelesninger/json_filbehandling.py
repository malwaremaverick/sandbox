import jsonmodul

planet = {"navn": "Merkur", "tyngdekraft": 3.73}
file_name = "planet.json"
string = "Dette er en string"

jsonmodul.skriv_json(planet, file_name)

innhold_fra_fil =  jsonmodul.les_json(file_name)
print(innhold_fra_fil)

print(innhold_fra_fil['navn'])