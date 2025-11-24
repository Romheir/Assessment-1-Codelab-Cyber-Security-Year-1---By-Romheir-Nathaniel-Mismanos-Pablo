def checks_even_odd(number): #this line of code defines the function called "checks_even_odd", and it accepts one input value thats called "number".
    if number % 2 == 0: #this line does what is called a modulus operation in python. "%" gives the remainder after the divison, and if the number divides evenly by 2 (which is zero remainder) then it is mathematically classified as even.
        return "This is an even number." #if in the case the condition is true, the function returns the message given. (p.s returning a vlue is crucial as it allows another part of the program to use the result.)
    else: 
        return "This is an odd number." #else if the condition was false, the number was not divisible evenly by 2, hence the false condition. What thise does is returns the message below, prompting that the number is odd.

def main(): #this defines the main function
    num = int(input("Please enter a number: ")) #this line does three tasks, to put it simply it asks the user for an input, receives the input as a STRING, then converts that string into an integer with the command int(). This conversion is essential to avoid type mismatch errors in the code which we do not want.
    result = checks_even_odd(num) #this calls the earlier function and stores the return value in the variable "result"
    print(result) #gives the output of the returned message to the console.

if __name__ == "__main__": #this ensures the program only runs AUTOMATICALLY when it is executed directly, not when it is imported. Typical python industry standard practice.
    main() #this is the trigger that starts the execution.

