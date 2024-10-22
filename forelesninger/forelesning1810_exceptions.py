try:
    tall1 = int(input("Skriv inn første tallet: "))
    tall2 = int(input("Skriv inn det andre tallet: "))
    svar = tall1 / tall2;
    print(svar)
    
except ValueError:
    print("Du skrev inn en ugyldig verdi!")

except NameError:
    print("Kunne ikke regne ut noe svar!")

except ZeroDivisionError:
    print("Du kan ikke dividere med 0!")
    
else:
    print("Du skrev inngyldig verdi!")
