import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
data = pd.read_csv('C:\\Users\\rimce\\Desktop\\CYB_1\\FDP\\flight_delay_predict.csv')


############


onehot_encoder = OneHotEncoder()

origin_encoded = onehot_encoder.fit_transform(data[['Origin']]).toarray()
encoded_df = pd.DataFrame(origin_encoded, columns=onehot_encoder.get_feature_names_out(['Origin']))
data_encoded = pd.concat([data.drop('Origin', axis=1), encoded_df], axis=1)

# Step 4: Save concatenated dataset back to CSV
data_encoded.to_csv('C:\\Users\\rimce\\Desktop\\CYB_1\\FDP\\flight_delay_predict.csv', index=False) 

'''
dest_encoded= onehot_encoder.fit_transform(data(['Dest'])).toarray()
dest_encoded_df = pd.DataFrame(dest_encoded, columns=onehot_encoder.get_feature_names_out(['Dest']))
data = data.join(origin_encoded_df).drop('Dest', axis=1)'''
####################

# Splitting the data into features and labels
X = data[['AirTime', 'Distance']]+ list(encoded_origin_df.columns) + list(encoded_dest_df.columns)]
y = data[['ArrDelayMinutes', 'is_delay']]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Building the neural network model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='linear'))

# Compiling the model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Training the model
model.fit(X_train, y_train, epochs=1, batch_size=32, verbose=1)

# Evaluating the model
score, accuracy = model.evaluate(X_test, y_test, verbose=0)

# Saving the model
model.save('/kaggle/working/model.h5')

# Real-time prediction
model = load_model('/kaggle/working/model.h5')


air_time = float(input("Enter Air Time in minutes: "))
distance = float(input("Enter Distance in miles: "))
orig=str(input("Enter city of origin: "))


user_input = np.concatenate([[air_time, distance], user_input_origin.flatten(), user_input_dest.flatten()]).reshape(1, -1)
user_input_scaled = scaler.transform(user_input)
predictions = model.predict(user_input_scaled)

if predictions[0][1] >= 0.5:
    print(f"The flight is delayed by {predictions[0][0]} minutes.")
else:
    print("The flight is not delayed.")


