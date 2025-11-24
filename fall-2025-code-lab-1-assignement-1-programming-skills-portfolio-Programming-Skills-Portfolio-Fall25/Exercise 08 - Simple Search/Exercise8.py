names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #this line of code stores the list of names given in the instructions.

search = input ("Please enter a name to search for: ") #this line of code asks the user what name (or person) they want to search for, and see if they are in the list.

found = False #this variable keeps track of whether the name is found.

for name in names: #this starts a loop that continues to go through each name in the list one by one.
    if name == search: #this line of code checks IF the name matches what the user has inputted
        print (f"{search} was found inside the list.") #this tells the user that the name is found. (this will only print if the name matches or is == to the names in the list.)
        found = True #finalizes that we successfully found a match with the user and the list.
        break #breaks the loop.
if not found:  #in the case it is not found, it will run the text below, prompting the user that the name was not found.
    print (f"{search} was not found inside the list.")

