correct_password = "12345" #this is the defined given password from the instructions.
attempts_left = 5 #this tracks how many tries the user has, starting at 5.

while attempts_left > 0: #this line of code starts a loop that will reapeat only IF the user still has attempts left to spare.
    password = input ("Please enter your password: ") #this asks the user to to type a password. This stores their answer in the variable "password"

    if password == correct_password: #IF in the case the password they typed is == or equak to the real correct password, it will be a success. If not, it will keep looping until no more tries are left.
        print("Access granted, Welcome user!") #this will be printed when the password is correct.
        break #this breaks the program and stops it.

    attempts_left -= 1 #this is quite simp;e. subtracts 1 from the remaining attempts left or counter.

    if attempts_left > 0: #this line of code checks if the user still has any tries left.
        print(f"This is the wrong password. You have {attempts_left} attempts left.") #this tells the user the password was wrong, andinforms the amount of attempts left.
    else:
        print("You have reached the maximum amount of attempts, the authorities have been alerted.") #else, if there is no more attempts this is what it shows and locks the user out.



