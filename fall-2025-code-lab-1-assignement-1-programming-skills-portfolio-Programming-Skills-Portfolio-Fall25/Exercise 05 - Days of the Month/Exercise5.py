months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} #this creates a dictionary labeled "months", each number from 1 to 12 represents a month, and the value is how many days that month NORMALLY has.

months_number = int(input("Please enter a month number from 1-12:")) #this asks the user to type a month number, the number given is stores in the variable months_number
 
if months_number < 1 or months_number > 12: #this line of code checks if the number is smaller than 1 or bigger than 12, and if it is smaller or bigger it's not a real month. Triggers the error message.
   print("This is an invalid month number.") #this is the error message given when the user inputs below 0 or above 12.
elif months_number == 2: #this line of code only runs if the input given by the user is not invalid, hence elif statement.
   leap = input("is this a leap year? (yes/no)").lower() #this asks the user if the year is a leap year, the command .lower() allows all types of the word "yes". So meaning it can be "YeS YES yes yEs Yes yES" etc.
   if leap == "yes": #if the user says yes, it prints the following below.
      print("The month february has 29 days in a leap year.")
   else:
      print("The month february has 28 days.") #if the user answers aything other than a "yes", it simply prints february 28.

else: 
   print(f"This month has {months[months_number]} days.") #this runs if the month is valid and isn't february, pretty simple. It does this by looking in the months number dictionary we made, then prints how many days it has.





