import Only_type as T

currency_rates = {
    "USD": 1.0,      # Base currency (e.g., USD)
    "INR": 84.47,     # 1 USD = 83 INR
    "EUR": 0.92,     # 1 USD = 0.92 EUR
    "GBP": 0.78,     # 1 USD = 0.78 GBP
    "AUD": 1.56,     # 1 USD = 1.56 AUD
    "CAD": 1.37,     # 1 USD = 1.37 CAD
    "JPY": 150.0,    # 1 USD = 150 JPY
    "CNY": 7.28,     # 1 USD = 7.28 CNY
    "AED": 3.67,     # 1 USD = 3.67 AED
    "SAR": 3.75,     # 1 USD = 3.75 SAR
    "ZAR": 18.8      # 1 USD = 18.8 ZAR
}


def Currency_Converter():
    '''This will Convert Your Currencies '''
    T.clear_screen()
    T.type_text(
        f"Welcome To Currency Converter \nAvailable Currency to Exchange with are : \n{currency_rates.keys()} ")
    amount = float(input("Enter Amount : "))
    source = input("Enter The Source Currency You have :  ").upper()
    target = input("Enter your Target Currency You Want : ").upper()
    if source not in currency_rates or target not in currency_rates:
        print("Invalid Currency Code. Please Check Available Currencies Again.")
    else:
        Converted = round(
            (amount * currency_rates[target]) / currency_rates[source], 2)
        T.type_text(f"You Will Have {Converted} {
                    target} for {amount} {source}")


Currency_Converter()
