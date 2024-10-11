import random

def myFunction():
    # Logikk
    return

def skrivHei():
    print("-------")
    print("--Hei--")
    print("-------")
    return
    
skrivHei()
skrivHei()
skrivHei()

def giEtTilfeldigTall(startverdi, stoppverdi):
    tilfeldigTall = random.randrange(startverdi, stoppverdi)
    return tilfeldigTall

nyttTall = giEtTilfeldigTall(10, 20)
print(nyttTall)

print(giEtTilfeldigTall(100, 1000))