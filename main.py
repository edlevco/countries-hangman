import random
countries = [["canada", "mexico", "argentina", "united states", "india"],
             ["spain", "portugal", "sweden", "poland", "germany"],
             ["mongolia", "china", "russia", "chile", "peru"]]
print("Welcome to the countries hang-man game!")
print("If you are stuck type '?' but it will cost 3 guesses")
levelInput = (int(input("What level do you want to play (1-3): "))) - 1
chosen_country = random.choice(countries[levelInput])
display = []
for letters in chosen_country:
    if letters == " ":
        display += " "
    else:
        display += "_"
guesses = 0
wordUnknown = True
letterGuess = ""

while wordUnknown:
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"Guesses: {guesses}")
    letterGuess = input("Guess a letter or country: ")
    if letterGuess == "?":
        guesses += 3
        while True:
            randNum = random.randint(0, len(chosen_country) - 1)
            if not chosen_country[randNum] == display[randNum]:
                display[randNum] = chosen_country[randNum]
                break
    for positions in range(len(chosen_country)):
        if chosen_country[positions] == letterGuess:
            display[positions] = letterGuess
    if "_" not in display or letterGuess == chosen_country:
        print(chosen_country)
        print(f"You got it correct, the country was {chosen_country}")
        print(f"It took you {guesses} guesses")
        wordUnknown = False
    guesses += 1
