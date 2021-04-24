import pickle
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

if __name__ == "__main__":
    print("\nReading data...")
    # Read the pinch data
    data = pd.read_csv("pinch_data.csv", index_col=None)
    
    print("\nExtracting features and labels...")
    # Separate features and labels
    #X = data[["S1_mean", "S2_mean"]].values
    X = data.drop(columns=["Label", "Timestamp", "S1_mean", "S2_mean"])
    y = data["Label"].values
    target_names = ['Non-grasp','Grasp']
    
    print("\nSplitting into test and train sets...")
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)
    
    print("\nTraining logistic regression...")
    # Create a logistic regression model
    lr_model = LogisticRegression(max_iter=100000).fit(X_train,y_train)
    # Query the model on the test set
    lr_pred = lr_model.predict(X_test)
    # Calculate the accuracy of the model
    lr_acc = accuracy_score(y_test, lr_pred)
    print(f"Accuracy: {lr_acc}")
    lr_mat = confusion_matrix(y_test,lr_pred)
    print(lr_mat)
    print(classification_report(y_test, lr_pred, target_names=target_names))
    
    print("\nTraing svm...")
    # Define a polynomial kernel for a svm
    kernel = 'poly'
    # Define a rbf kernel for a svm
    #kernel = 'rbf'
    # Create a svm model using the predefined kernel
    svm_model = svm.SVC(kernel=kernel, gamma=10, max_iter=100000).fit(X_train,y_train)
    # Query the model on the test set
    svm_pred = svm_model.predict(X_test)
    # Calculate the accuracy of the model
    svm_acc = accuracy_score(y_test, svm_pred)
    print(f"Accuracy: {svm_acc}")
    svm_mat = confusion_matrix(y_test,svm_pred)
    print(svm_mat)
    print(classification_report(y_test, svm_pred, target_names=target_names))
    
    print("\nTraining random forest...")
    # Create a random forest model
    rf_model = RandomForestClassifier(max_depth=100000).fit(X_train, y_train)
    # Query the model on the test set
    rf_pred = rf_model.predict(X_test)
    # Calculate the accuracy of the model
    rf_acc = accuracy_score(y_test, rf_pred)
    print(f"Accuracy: {rf_acc}")
    rf_mat = confusion_matrix(y_test,rf_pred)
    print(rf_mat)
    print(classification_report(y_test, rf_pred, target_names=target_names))
    
    if input("Save models? y/n: ") == "y":
        pickle.dump(lr_model, open("logistic_regression", 'wb'))
        pickle.dump(svm_model, open("svm", 'wb'))
        pickle.dump(rf_model, open("random_forest", 'wb'))
    