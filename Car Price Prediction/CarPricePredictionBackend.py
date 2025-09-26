# CarPricePredictionBackend.py
# Backend logic for Car Price Prediction

import random

class CarPricePredictor:
    def predict(self, features: dict) -> float:
        """
        Predict car price based on features using a dummy formula.
        Real implementation would use ML model trained on dataset.
        """
        base_price = 20000
        year_adjust = (2025 - int(features.get("year", 2020))) * -500
        mileage_adjust = int(features.get("mileage", 0)) * -2
        brand_factor = random.randint(-2000, 3000)
        return base_price + year_adjust + mileage_adjust + brand_factor
