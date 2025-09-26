# input.py
# Handles user input for Currency Converter

def get_inputs():
    """
    Collects amount, source currency, and target currency.
    :return: (amount, from_currency, to_currency)
    """
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (USD/INR/EUR): ").upper()
    to_currency = input("To currency (USD/INR/EUR): ").upper()
    return amount, from_currency, to_currency
