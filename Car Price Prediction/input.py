# input.py
# Handles user input for Car Price Prediction

def get_inputs():
    features = {}
    features["brand"] = input("Enter car brand: ")
    features["model"] = input("Enter car model: ")
    features["year"] = input("Enter manufacture year: ")
    features["mileage"] = input("Enter mileage: ")
    return features
