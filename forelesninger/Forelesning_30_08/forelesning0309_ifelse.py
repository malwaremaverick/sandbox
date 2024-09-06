x = 3
y = 300

er_X_storre_enn_y = x > y
# print(er_X_storre_enn_y)

if (er_X_storre_enn_y == True):
    print(f"{x} er større enn {y}")
    
else: 
    print(f"{x} er ikke større enn {y}")
#------------------
number = -10

if (number > 0):
    print(f"{number} er et positivt tall.")
elif (number < 0):
    print(f"{number} er et negativt tall.")
elif (number < 0):
    print("Dette er test 2")
else:
    print(f"{number} er 0")
    
navn1 = "piotr"
navn2 = "PiOTr"

if (navn1.lower() == navn2.lower()):
    print("Navnene er like")
else:
    print("Navnene er ikke like")