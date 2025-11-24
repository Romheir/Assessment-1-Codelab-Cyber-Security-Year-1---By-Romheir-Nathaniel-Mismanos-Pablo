name = input("Please enter your name: ") 
#This is to have the user enter their name.

hometown = input("Please enter your designated hometown: ")
#This asks the user to enter their hometown, both use the input command to do this.

while True: #This code starts what is called an "infinite loop"

    # the block of code inside this command will continue to run over and over.

    #until it is manually stopped using the "break" command.

    age_input = input("Please enter your age:") 
    #this line of code requests the user for the users age.
    #whatever input is given is stored as a "string" in python.

    try:
        age = int(age_input) #this line of code tries to convert the string into an integer.
        break #thus if the user enters "16" the number becomes 16 and the loop is stopped using the "break" command.
    except ValueError: #this code only runs if the conversion fails, like if the user enters sixteen instead. This cannot become an integer.
        print("I am sorry, the age you have given must be a number. Please try again.") #So thus, python triggers the ValueError command.
        #the code then jumps and prints the following above. It will continue to loop until the proper format is given.

info = { "name": name, "hometown": hometown, "age": age}

print(info["name"], info["hometown"], info ["age"], sep="\n")
