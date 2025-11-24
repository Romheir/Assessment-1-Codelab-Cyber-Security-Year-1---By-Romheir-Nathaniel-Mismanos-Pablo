score = 0 #we will start with this code that keep tracks of the how many questions the user gets right.

questions = {"France": "paris", "Spain": "madrid", "Germany": "berlin", "Italy": "rome", "Portugal": "lisbon", "Belgium": 
             "brussels", "Netherlands": "amsterdam", "Sweden": "stockholm", "Greece": "athens", "Austria": "vienna"}
#since we are going for the advance requirements, I am taking my time to list 10 countries and their captial. This stores them in this dictionary.

for country, capital in questions.items(): #this code is the loop, it will go through each pair in the dictionary (the country and capital)
# and in each time, the code will take a country and the capital its listed with.
    answer = input(f"What is the capital of {country}?").lower()

    if answer == capital: #this code means IF it matches the correct answer hence "==" it will print the following below and increase the score."
        print("Your answer is Correct!")
        score += 1 #this increases the score by 1 after the user gets the correct answer
    else: #but if it does not match the correct answerm it will print the following below AND show the correct answer.
        print(f"Your answer is wrong. The correct answer is {capital.capitalize()}.")

print(f"Your final score is: {score} / {len(questions)}") #This line of code shows how many the user got right.





