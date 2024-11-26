import logo
import game_data
import random 


def highlower():
    print(logo.higher_lower)
    A = random.choice(game_data.data)
    print(f"Compare A : {A['name']}, a {A['description']}, from {A['country']} " )
    print(logo.vs)
    B = random.choice(game_data.data)
    print(f"Compare B : {B['name']}, a {B['description']}, from {B['country']} " )
    Guess = input("Who has more followers? Type 'A' or 'B': ")
    if Guess['follower_count'] > B['follower_count']:
        print("A is bigger")
    else:
        print("B is bigger")

highlower()
