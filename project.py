import numpy as np
from sklearn.linear_model import LinearRegression

area = np.array([500, 1000, 1500, 2000]).reshape(-1, 1)
price = np.array([100000, 200000, 300000, 400000])

model = LinearRegression()
model.fit(area, price)

predicted_price = model.predict([[1200]])

print("Predicted Price:", predicted_price)
