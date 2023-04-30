import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
from sklearn.model_selection import train_test_split
import time

# load the boston dataset
def Classification():
   

# Read the CSV file into a Pandas DataFrame
    data = pd.read_csv('mock_data_all.csv')

    X = data.iloc[:, 2:-1].values
    y = data.iloc[:, -1].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model and fit the training data
    model = LinearRegression().fit(X_train, y_train)

    # Predict the output values for the testing data
    y_pred = model.predict(X_test)
    
    y_pred = [ round(elem) for elem in y_pred ]
    print(y_pred)

    # Calculate the model accuracy on the testing data
    accuracy = r2_score(y_test, y_pred)

# Predict the output values for the input data
    

    print(f"Model Accuracy: {accuracy}")

    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))

    print("Accuracy is ",accuracy)
    return accuracy

def main():
        accuracy =  Classification()

if __name__ == "__main__":
        start = time.time()
        main()
        end = time.time()
        print(f"Runtime of the program is {end - start}")
