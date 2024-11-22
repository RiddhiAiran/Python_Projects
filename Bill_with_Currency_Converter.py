import Only_type as T
import Tip_Calculator as TC
import Currency_Converter as CC


def Bill_with_Currency_Converter():
    T.clear_screen()
    T.type_text(f"Welcome To Bill with Currency Converter!")
    TC.Tip_Calculator()

    T.type_text(
        f'Do you want to Convert Your Bill Currency to Any Other Currency ? ')
    convert = input("Type : Y/N").upper()
    if convert == 'Y':
        CC.Currency_Converter()
    else:
        T.type_text("Thank You For Being Here!")
