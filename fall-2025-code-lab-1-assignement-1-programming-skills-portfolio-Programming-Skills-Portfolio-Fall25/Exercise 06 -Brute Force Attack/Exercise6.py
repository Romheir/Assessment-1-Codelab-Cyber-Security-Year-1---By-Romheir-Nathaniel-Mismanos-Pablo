correct_password = "12345"
attemps_left = 5

while attemps_left > 0:
    password = input ("Please enter your password: ")

    if password == correct_password:
        print("Access granted, Welcome user!")
        break

    attempts_left -= 1

    if attempts_left > 0: 
        print(f"This is the wrong password. You have {attempts_left} attempts left.")
    else:
        print("You have reached the maximum amount of attempts, the authorities have been alerted.")
