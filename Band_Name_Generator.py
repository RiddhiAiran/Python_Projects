import Only_type as T


def band_name():
    '''Helps users create a unique and fun band name by
    combining two inputs. Ask users for their favorite city
    and an animal or color. Combine these inputs to form a 
    quirky band name.'''
    T.clear_screen()
    T.type_text(
        "Welcome, To Band Name Generator! We will Generate a Band Name For You 🎸")
    pet = input("Enter Your Favorite Animal or Color : ").title()
    city = input("Enter Your Favorite City Name : ").title()

    T.type_text(f'Wow ! Your Band Name Can be {pet} {city}')


if __name__ == "__main__":
    band_name()
