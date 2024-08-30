mitt_jordVekt = input("Hva er din vekt på jorden?")
mitt_jordVekt = float(mitt_jordVekt)
jord_gravitet = 9.807
maane_gravitet = 1.622
maane_vekt = mitt_jordVekt / jord_gravitet * maane_gravitet

def vektKalkulator():
    global mitt_jordVekt
    global jord_gravitet
    global maane_gravitet
    global maane_vekt
    mitt_jordVekt = float(mitt_jordVekt)
    print(mitt_jordVekt)
    print(f"Din vekt på månen er {maane_vekt}")

vektKalkulator()
