import random

def main():
    #Take input from user
    firstname = input("What is your name? ").strip()

    #split name if space found to separate first name
    if " " in firstname:
        firstname, lastname = firstname.split(" ")

    #take year of birth input from user
    year = int(input(f"{firstname.title()}?? What an awesome name! What year were you born? "))
    oldometer(year, firstname)
    


def oldometer(dob, name):
    #random insult generation
    
    phrase1 = "Oh....I am so sorry, I didn't realise...You poor thing"
    phrase2 = "Holy fucking shit that is old"
    phrase3 = "Oh gosh, how rude of me, would you like a walker to assist you?"
    phrase4 = "Woah, thought you were way older than that...there you go!"
    phrase5 = "Huh....I thought I could smell mould!"

    array = [phrase1, phrase2, phrase3, phrase4, phrase5]


    # print to screen
    if (dob <= 1992) and ("ayden" in name) :
        print((random.choice(array)))
    else:
        print(f"So you were born in {dob}? Wow, still so incredibly young and youthful!! I would have guessed younger!")


main()