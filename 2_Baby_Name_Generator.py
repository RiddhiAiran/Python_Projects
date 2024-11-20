import Type_Like_GPT as T


def Baby_Name_Generator():
    '''Generates baby name suggestions based on the
        parents' names or other preferences like gender, 
        origin, or meaning.'''
    T.type_text("Welcome to Baby Name Generator!")
    Gender = input("Enter Baby's Gender (M/F/O): ").lower()
    Father = input("Enter Father's Name : ").title()
    Mother = input("Enter Mother's Name : ").title()
    T.type_text(f"Your Baby Name Can be : {Father[:2]}{Mother[-3:]}")


Baby_Name_Generator()
