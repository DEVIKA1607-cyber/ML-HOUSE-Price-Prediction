NAME : D DEVIKA

REG NO: 212224100010

## Title
House Price Prediction using Machine Learning

## Introduction
This project predicts house prices based on area using Linear Regression.
House Price Prediction is a popular machine learning project where we use data (like location, size, number of rooms, etc.) to predict the price of a house. It helps buyers, sellers, and real estate companies make better decisions.

## Objective

The main objectives of this project are:

To predict house prices accurately based on different features.
To analyze factors that affect house prices (e.g., location, area, number of bedrooms).
To apply machine learning algorithms to real-world data.
To build a model that can estimate prices automatically.
To improve decision-making in the real estate sector.

## Technology Used
- Python
- NumPy
- Scikit-learn

## Algorithm

Step 1: Start
Begin the process

Step 2: Import Libraries
Import required libraries like:
NumPy
Linear Regression from sklearn

Step 3: Prepare Data
Define input data (area of houses)
Define output data (price of houses)

Step 4: Reshape Data
Convert input data into required format for the model

Step 5: Create Model
Create a Linear Regression model

Step 6: Train Model
Fit the model using input (area) and output (price) data

Step 7: Predict Output
Give new input (e.g., area = 1200)
Predict the corresponding price

Step 8: Display Result
Print the predicted price

## Code

import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Input data (Area vs Price)
area = np.array([500, 1000, 1500, 2000]).reshape(-1, 1)
price = np.array([100000, 200000, 300000, 400000])

# Step 2: Create model
model = LinearRegression()
model.fit(area, price)

# Step 3: Predict price for new area
predicted_price = model.predict([[1200]])

# Step 4: Output
print("Predicted Price:", predicted_price)

## Output
Predicts price for given area input.
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/d89dcee9-5a77-4f03-a925-a8fda12001d9" />

## Machine Learning Approach

Step-by-step process:

Data Collection

Collect housing data from datasets (CSV, Kaggle, etc.)

Data Preprocessing

Handle missing values

Convert categorical data (like location) into numbers

Normalize/scale data if needed

Feature Selection

Choose important features that influence price

Model Selection

# Common algorithms:

Linear Regression (most common)

Decision Tree

Random Forest

Gradient Boosting

Model Training

Train the model using training data

Model Testing

Test accuracy using test data

Prediction

Predict house prices for new inputs

## Example

If input is:

Area = 1200 sq.ft

Bedrooms = 3

Location = City Center

 Model predicts: ₹75 Lakhs (example)

## Advantages

Saves time in price estimation

Reduces human error

Helps in investment decisions

Useful for real estate companies

## Conclusion
This project shows how Machine Learning can be used to predict values from data. 
Linear Regression is easy to understand and useful for basic data analytics problems.
