import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression  

def heart_disease(age, sex, chest_pain_type, resting_blood_pressure, cholesterol, fasting_blood_sugar, maximum_heart_rate_achieved, exercise_induced_angina):
    
    age = int(age)
    sex = 1 if sex == 'Male' else 0
    dict = {'Typical Angina' : 1, 'Atypical Angina' : 2, 'Non-Anginal Pain' : 3, 'Asymptomatic' : 4}
    chest_pain_type = dict[chest_pain_type]
    resting_blood_pressure = int(resting_blood_pressure)
    cholesterol = int(cholesterol)
    fasting_blood_sugar = 1 if fasting_blood_sugar == 'True' else 0
    maximum_heart_rate_achieved = int(maximum_heart_rate_achieved)
    exercise_induced_angina = 1 if exercise_induced_angina == 'True' else 0

    parameters = (age, sex, chest_pain_type, resting_blood_pressure, cholesterol, fasting_blood_sugar, maximum_heart_rate_achieved, exercise_induced_angina)
    
    heart_data = pd.read_csv("C:/Users/Admin/Downloads/heart_Data_2.csv")

    # Splitting the features and targets
    X = heart_data.drop(columns = 'target', axis = 1)
    Y = heart_data['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, stratify = Y, random_state = 2)
    
    model = RandomForestClassifier()
    model.fit(X_train, Y_train)

    input_data = parameters   # It a tuple data type

    # Change input data to a numpy array (as it is easy to re-shape a numpy array rather than a tuple)
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    prediction = prediction.tolist()
    
    return(prediction[0])


def diabetes(glucose, blood_pressure, insulin, body_mass_index, age):
    glucose = int(glucose)
    blood_pressure = int(blood_pressure)
    insulin = int(insulin)
    body_mass_index = float(body_mass_index)
    age = int(age)

    parameters = (glucose, blood_pressure, insulin, body_mass_index, age)

    diabetes_data = pd.read_csv("C:/Users/Admin/Downloads/diabetes_data.csv")

    X = diabetes_data.drop(columns = 'Outcome', axis = 1)
    Y = diabetes_data['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

    # Training the model
    model = LogisticRegression()

    model.fit(X_train, Y_train)

    input_data = parameters  # It a tuple data type

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    prediction = prediction.tolist()
    
    return (prediction[0])

def liver_disease(age, gender, total_bilirubin, alkaline_phosphotase, alamine_aminotransferase, total_protiens, albumin) :
    
    age = int(age)
    gender = 1 if gender == 'Male' else 0
    total_bilirubin = float(total_bilirubin)
    alkaline_phosphotase = int(alkaline_phosphotase)
    alamine_aminotransferase = int(alamine_aminotransferase)
    total_protiens = float(total_protiens)
    albumin = float(albumin)

    parameters = (age, gender, total_bilirubin, alkaline_phosphotase, alamine_aminotransferase, total_protiens, albumin)
    
    liver_data = pd.read_csv('C:/Users/Admin/Downloads/LiverDiseaseDataset.csv')

    # Separating the data and labels
    X = liver_data.drop(columns = 'target', axis = 1)
    Y = liver_data['target']

    # Splitting training data and test data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

    # Training the model
    model = RandomForestClassifier()

    model.fit(X_train, Y_train)

    input_data = parameters   # It a tuple data type

    # Change input data to a numpy array (as it is easy to re-shape a numpy array rather than a tuple)
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)

    prediction = prediction.tolist()
    
    return (prediction[0])
