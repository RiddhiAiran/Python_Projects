import Type_Like_GPT as T


def Tip_Calculator():
    T.type_text("Welcome To Tip Calculator!")
    Amount = float(input("Enter Total Bill Amount : "))
    Tip = float(input("Enter Tip You want to give :  "))
    Split = int(
        input("Enter How many people will Split the bill (atleast 1) : "))
    Each_pay = round((Amount+Tip)/Split, 2)
    T.type_text(f'Total Bill Including Tip will be {
                Amount+Tip} and {Split} person Should Pay {Each_pay} Each')


Tip_Calculator()