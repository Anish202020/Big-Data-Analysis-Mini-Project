# Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense,LSTM
from keras import metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("wind-speed.csv")
L = len(df)
print(L)

# Prepare Y
Y = df.iloc[:, 3].values  # Convert to 1D array
plt.plot(Y)
plt.show(block=False)

# Create X1, X2, X3
X1 = Y[0:L-5]
X2 = Y[1:L-4]
X3 = Y[2:L-3]

# Stack and transpose X
X = np.vstack((X1, X2, X3)).T  # Stack vertically and transpose

# Prepare Y for LSTM
Y = Y[3:L-2]

# Scale X
sc = MinMaxScaler()  # No parameters
sc.fit(X)
X = sc.transform(X)

# Scale Y
sc1 = MinMaxScaler()
Y = Y.reshape(-1, 1)  # Reshape Y to be 2D
sc1.fit(Y)
Y = sc1.transform(Y)

# Reshape X for LSTM
X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Define the LSTM model
model = Sequential()
model.add(LSTM(10, activation='tanh', input_shape=(1, 3), recurrent_activation='hard_sigmoid'))
model.add(Dense(1))

# Compile the model
model.compile(loss="mean_squared_error", optimizer='rmsprop', metrics=[metrics.mean_squared_error])

# Fit the model
model.fit(X_train, Y_train, epochs=25, verbose=2)

# Make predictions
predict = model.predict(X_test)

# Plot predictions
plt.figure(2)
plt.scatter(Y_test, predict)
plt.xlabel("Real Data")
plt.ylabel("Predicted Data")
plt.show(block=False)

plt.figure(3)
plt.plot(Y_test, label="Real Data")
plt.plot(predict, label="Predicted Data")
plt.legend()
plt.show()
