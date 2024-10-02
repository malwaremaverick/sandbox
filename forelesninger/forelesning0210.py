brettspill = {'tittel': 'dixit',
              'spilletid': 30,
              'aldersgrense': 8}

print(brettspill)
print()
print(brettspill['spilletid'])

brettspill['spilletid'] = 40

print(brettspill)

print(brettspill.get('spilletid'))
brettspill['beskrivelse'] = 'Give the perfect clue so most (not all) players guess the right surreal image card'
print(brettspill)

brettspill.pop('spilletid')
print(brettspill)

del brettspill['spilletid']
print(brettspill)