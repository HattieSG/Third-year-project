from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

if __name__ == "__main__":
    # Read the 
    data = pd.read_csv("pinch_data.csv", index_col=None)
    
    # Separate features and labels
    #X = data[["S1_mean", "S2_mean"]].values
    #y = data["Label"].values
    X, y = load_iris(return_X_y=True)
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    # Create a logistic regression model
    lr_model = LogisticRegression().fit(X_train,y_train)
    # Query the model on the test set
    lr_pred = lr_model.predict(X_test)
    # Calculate the accuracy of the model
    lr_acc = accuracy_score(y_test, lr_pred)
    
    # Define a polynomial kernel for a svm
    kernel = 'poly'
    # Define a rbf kernel for a svm
    #kernel = 'rbf'
    # Create a svm model using the predefined kernel
    svm_model = svm.SVC(kernel=kernel, gamma=10).fit(X_train,y_train)
    # Query the model on the test set
    svm_pred = svm_model.predict(X_test)
    # Calculate the accuracy of the model
    svm_acc = accuracy_score(y_test, svm_pred)
    
    # Create a random forest model
    rf_model = RandomForestClassifier().fit(X_train, y_train)
    # Query the model on the test set
    rf_pred = rf_model.predict(X_test)
    # Calculate the accuracy of the model
    rf_acc = accuracy_score(y_test, rf_pred)
    
    