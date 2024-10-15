from math import log

def hundealder_til_menneskealder(hundealder):
    menneskealder = 16 * log(hundealder) + 31
    return menneskealder

print(hundealder_til_menneskealder(50))
menneskes_alder = hundealder_til_menneskealder(10)
print(menneskes_alder)

def inkludert_moms(pris, moms=0.25):
    pris_med_moms = pris + pris * moms
    return pris_med_moms

pris_uten_moms = 100

print(inkludert_moms(pris_uten_moms))