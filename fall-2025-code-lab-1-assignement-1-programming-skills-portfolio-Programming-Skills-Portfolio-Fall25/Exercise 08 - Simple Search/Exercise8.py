names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search = input ("Please enter a name to search for: ")

found = False

for name in names:
    if name == search:
        print (f"{search} was found inside the list.")
        found = True
        break
if not found:
    print (f"{search} was not found inside the list.")
