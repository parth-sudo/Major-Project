import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression  

def heart_disease(parameters):
    heart_data = pd.read_csv("C:/Users/Admin/Downloads/heart_Data_2.csv")
    # heart_data.head()

    # Splitting the features and targets
    X = heart_data.drop(columns = 'target', axis = 1)
    Y = heart_data['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, stratify = Y, random_state = 2)
    
    model = RandomForestClassifier()

    model.fit(X_train, Y_train)

    # YAHA PE VO DATA AAYEGA JO USER INPUT KAREGA

    input_data = parameters   # It a tuple data type

    # Change input data to a numpy array (as it is easy to re-shape a numpy array rather than a tuple)
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)

    return prediction


def diabetes(parameters):
    diabetes_data = pd.read_csv("C:/Users/Admin/Downloads/diabetes_data.csv")

    X = diabetes_data.drop(columns = 'Outcome', axis = 1)
    Y = diabetes_data['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

    # Training the model

    model = LogisticRegression()

    model.fit(X_train, Y_train)

    # YAHA PE VO DATA AAYEGA JO USER INPUT KAREGA

    input_data = (115, 57, 94, 27.7, 42)    # It a tuple data type

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)

    return prediction
