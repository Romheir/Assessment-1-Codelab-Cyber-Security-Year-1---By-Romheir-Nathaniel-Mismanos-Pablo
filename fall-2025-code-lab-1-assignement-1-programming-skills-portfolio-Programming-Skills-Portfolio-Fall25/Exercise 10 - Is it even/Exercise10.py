def checks_even_odd(number):
    if number % 2 == 0:
        return "This is an even number."
    else: 
        return "This is an odd number."

def main():
    num = int(input("Please enter a number: "))
    result = checks_even_odd(num)
    print(result)

if __name__ == "__main__":
    main()
