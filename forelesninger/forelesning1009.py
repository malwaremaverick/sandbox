planeter = ["Jorden", "Saturn", "Pluto", "Venus", "Uranus", "Merkur"]
print(planeter[0])

planeter[3] = "Mars"


planeter.append("Neptun")
planeter.append("Pluto")

planeter.insert(4, "Jupiter")

planeter.pop()
planeter.pop(3)

planeter.remove("Saturn")

print("Midlertidig sortert liste:")
print(sorted(planeter))
print("Originalen: ")
print(planeter)

print("Andre koder: ")
planeter.reverse()
print(planeter)

planeter.sort()
print(planeter)

planeter.sort(reverse=True)
print(planeter)



# random_list = ["Europe", 7, ["Ny liste", 23, "med mye elementer"], "Bil"]

# print(random_list[2])
# print(random_list[2][2])

# random_list[2].insert(1, "Spørsmål i timen")



