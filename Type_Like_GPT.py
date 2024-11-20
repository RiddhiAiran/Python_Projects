import os
import time


def clear_screen():
    os.system('clear')


def type_text(message):
    clear_screen()
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(0.03)
    print()
