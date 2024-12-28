from flask import Flask, render_template, request
import joblib
import numpy as np
#import flask
app = Flask(__name__)

 #Load the trained model
model = joblib.load('car_price_model.pkl')

# Global lists for dropdown options
CAR_NAMES = ['Maruti 800 AC', 'Honda City', 'Hyundai Verna']  # Add all car names
FUEL_TYPES = ['Petrol', 'Diesel', 'CNG']
SELLER_TYPES = ['Individual', 'Dealer']
TRANSMISSIONS = ['Manual', 'Automatic']
OWNERS = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner']

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction page route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.form
        try:
            # Preprocess the input
            processed_features = preprocess_input(data)

            # Predict the car price
            prediction = model.predict(processed_features)
            # Convert prediction to a Python float and round to two decimal places
            predicted_price = round(float(prediction[0][0]/100000), 2)
            print(predicted_price)
            # Render the prediction page with the result
            return render_template(
                'predict.html',
                car_names=CAR_NAMES,
                fuel_types=FUEL_TYPES,
                seller_types=SELLER_TYPES,
                transmissions=TRANSMISSIONS,
                owners=OWNERS,
                predicted_price=f"{predicted_price} lakhs"
            )
        except Exception as e:
            return render_template(
                'predict.html',
                car_names=CAR_NAMES,
                fuel_types=FUEL_TYPES,
                seller_types=SELLER_TYPES,
                transmissions=TRANSMISSIONS,
                owners=OWNERS,
                error=str(e)
            )
    return render_template(
        'predict.html',
        car_names=CAR_NAMES,
        fuel_types=FUEL_TYPES,
        seller_types=SELLER_TYPES,
        transmissions=TRANSMISSIONS,
        owners=OWNERS
    )

# Function to preprocess input data
def preprocess_input(data):
    # Example preprocessing
    features = np.zeros((1, 127))  # Adjust size based on your model's requirements
    
    # Process the inputs (example shown for simplicity)
    features[0, 0] = float(data['Present_Price'])
    features[0, 1] = float(data['Kms_Driven'])
    features[0, 2] = float(data['Year'])
    
    # Add further processing for encoded features like 'Car_Name', 'Fuel_Type', etc.
    # Ensure correct feature mapping based on the trained model
    
    return features

if __name__ == '__main__':
    app.run(debug=True)
