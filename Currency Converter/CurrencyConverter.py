# CurrencyConverter.py
# Main runner file for Currency Converter project

from CurrencyConverterBackend import Converter
import input

def main():
    amount, from_currency, to_currency = input.get_inputs()
    converter = Converter()
    result = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")

if __name__ == "__main__":
    main()
