import random
import Only_type as T

girls_names = [
    "Aaradhya", "Anaya", "Diya", "Ira", "Kavya", "Mira", "Riya", "Saanvi", "Tanvi", "Vaishnavi"
]

boys_names = [
    "Aarav", "Aditya", "Ishaan", "Karan", "Nishant", "Rohan", "Shaurya", "Vivaan", "Yuvraj", "Zayan"
]

unisex_names = [
    "Aarya", "Dev", "Harsha", "Kiran", "Krishna", "Manu", "Nirav", "Sagar", "Shiv", "Vishwa"
]


def Baby_Name_Generator():
    '''Generates baby name suggestions based on the
        parents' names or other preferences like gender, 
        origin, or meaning.'''
    T.clear_screen()
    T.type_text("Welcome to Baby Name Generator!")

    Gender = input("Enter Baby's Gender (M/F/O): ").upper()
    Father = input("Enter Father's Name: ").title()
    Mother = input("Enter Mother's Name: ").title()
    Initials = input("Enter The Initial You want in Name: ").upper()

    # Filter names based on gender and initials
    if Gender == "M":
        filtered_names = [
            name for name in boys_names if name.startswith(Initials)]
    elif Gender == "F":
        filtered_names = [
            name for name in girls_names if name.startswith(Initials)]
    elif Gender == "O":
        filtered_names = [
            name for name in unisex_names if name.startswith(Initials)]
    else:
        T.type_text('Please write a valid input!')
        return

    # Handle case where no names match the initials
    if not filtered_names:
        T.type_text(
            "Sorry, no names found with that initial. Here are some random suggestions:")
        if Gender == "M":
            filtered_names = random.sample(boys_names, 4)
        elif Gender == "F":
            filtered_names = random.sample(girls_names, 4)
        elif Gender == "O":
            filtered_names = random.sample(unisex_names, 4)

    # Get up to 4 random suggestions from the filtered names
    suggestions = random.sample(filtered_names, min(4, len(filtered_names)))
    T.type_text(f"Some Suggestions for Your Baby: {', '.join(suggestions)}")


if __name__ == "__main__":
    Baby_Name_Generator()
