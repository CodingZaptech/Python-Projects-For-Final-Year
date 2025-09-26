# CarPricePrediction.py
# Main runner file for Car Price Prediction

from CarPricePredictionBackend import CarPricePredictor
import input

def main():
    features = input.get_inputs()
    predictor = CarPricePredictor()
    price = predictor.predict(features)
    print(f"Predicted Car Price: ${price:.2f}")

if __name__ == "__main__":
    main()
