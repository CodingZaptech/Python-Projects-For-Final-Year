# CurrencyConverterBackend.py
# Backend logic for Currency Converter

class Converter:
    def __init__(self):
        # Example static rates for demo (1 base = value in target)
        self.rates = {
            "USD": {"INR": 83, "EUR": 0.92},
            "INR": {"USD": 0.012, "EUR": 0.011},
            "EUR": {"USD": 1.09, "INR": 90}
        }

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency in self.rates and to_currency in self.rates[from_currency]:
            return round(amount * self.rates[from_currency][to_currency], 2)
        return -1
