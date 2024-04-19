while True:
    import random  # This is to generate random module
    secret_number = random.randint(1,100 )  # Generate random number between 1-100
    user_input = int(input("Guess a number between 1 and 100: ")) #for input
    if user_input == secret_number: # If guess matches the secret number
        print("Your guess is correct.")
    elif user_input> secret_number: # If guess is too high
        print("Your guess is too high")
    elif user_input< secret_number: # If guess is too low
        print("you guess is too low")
    else:
        print("Your guess is too low") # Printing the actual number if guess was wrong
    print("the number was",secret_number)

