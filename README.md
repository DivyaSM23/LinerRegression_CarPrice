# Car Price Predictor

## Project Description

The *Car Price Predictor* is a web application that predicts the price of a used car based on several input features such as car name, year, kilometers driven, fuel type, seller type, transmission, and number of previous owners. This project uses machine learning to train a model on historical car price data and then deploys the model using a web interface, allowing users to easily input details of a car and receive a predicted price.

## Technologies Used

### Machine Learning

- *Algorithm: The model uses a regression algorithm to predict the price of cars. Specifically, a **Random Forest Regressor* model is trained to understand the relationship between car attributes and the car's price.
- *Library Used*: 
  - *scikit-learn*: The primary library used for training the machine learning model.
  - *pandas* and *numpy*: For data manipulation and processing.
  - *matplotlib*: For visualizing data insights and model performance.
  
### Web Application

- *Framework*: Flask is used for creating the web application and serving the machine learning model.
- *Frontend: The frontend is designed using **HTML, **CSS, and **Bootstrap* for a responsive and visually appealing user interface. The form accepts car details and displays the predicted price once the user submits the form.
  
---

## Features

- *Car Price Prediction*: Based on input car details, the model predicts the price of the car.
- *Responsive UI*: A user-friendly interface that adapts to different screen sizes.
- *Machine Learning Backend*: Trained model on real-world car data, providing accurate predictions.
- *No Scrolling Needed*: The form and result display are designed to be within a single view with no scrolling required.

---

## Requirements

Before setting up the project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

---

## Installation and Setup

### 1. Clone the Repository

To get started, first clone this repository to your local machine:

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 3. Create a virtual environment and activate it (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

Then install the required dependencies:


```bash
pip install -r requirements.txt
```


### 3. Run the Flask Web Application
Start the Flask server to run the web app:

```bash
python app.py
```

This will start a local development server, typically accessible at http://127.0.0.1:5000/. Open this URL in your browser to access the Car Price Predictor web app.

---

## How the Model Works
The model works by taking the following input features and predicting the car price:
```
Car Name: The brand or model name of the car.
Year: The manufacturing year of the car.
Present Price: The current price of the car in lakhs.
Kms Driven: The total number of kilometers the car has been driven.
Fuel Type: The type of fuel used by the car (e.g., petrol, diesel).
Seller Type: Whether the seller is an individual or a dealer.
Transmission: The type of transmission the car has (automatic or manual).
Owner: The number of previous owners.
```
After receiving these inputs, the trained Random Forest Regressor model makes predictions based on the relationships it learned from historical data.

Web Application
The web interface provides an intuitive form where users can input the details of the car they wish to predict the price for. Once the user submits the form, the model predicts the car price and displays it.

How to Use the Web App
Navigate to the app's URL (http://127.0.0.1:5000/).
Fill out the car details in the form.
Click Predict.
The predicted price will be displayed at the bottom of the form.
Example Prediction
Here’s a sample input and output for a prediction:

Car Name: Toyota Corolla
Year: 2018
Present Price: 8.5
Kms Driven: 50000
Fuel Type: Petrol
Seller Type: Individual
Transmission: Manual
Owner: 1
Predicted Price: ₹7,50,000
