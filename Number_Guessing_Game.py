import Only_type as T
import random 
Easy_level_turns = 5
Hard_level_turns = 10
answer = random.randint(1,100)

def Check_number(answer, Guess):
    if answer == Guess:
        return "Correct"
    elif answer < Guess:
        return "Too High!"
    elif answer > Guess:
        return "Too Low!"
    else:
        return f"You got This : {answer}"

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
        return Easy_level_turns
    else:
        return Hard_level_turns

def Guess_number():
    T.clear_screen()
    T.type_text("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    difficulty = set_difficulty()
    T.type_text(f"You got {difficulty} Lives for this game!")
    T.type_text(f"Pss! the number is {answer}")
    while difficulty != 0:
        Guess = int(input("What's your Guess : "))
        number_guessed = Check_number(answer,Guess)
        print(number_guessed)
        if number_guessed == "Correct":
            print("You win")
            break
        else:
            difficulty -= 1
            print(f"Sorry You loose a Life, {difficulty} Remaining!")


Guess_number() 
            
    
