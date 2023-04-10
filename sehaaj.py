import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
 
 # Load the data
data = pd.read_csv("credit_risk_data1.csv")
 
 # Preprocess the data
data["income"] = np.log(data["income"])
data = pd.get_dummies(data, columns=["education", "marital_status", "housing", "default", "loan"], drop_first=True)
 
 # Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
     data.drop(columns=["credit_risk"]), data["credit_risk"], test_size=0.3, random_state=42
 )
 
 # Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
 
 # Train the logistic regression model
clf = LogisticRegression(random_state=42)
clf.fit(X_train_scaled, y_train)
 
 # Make predictions on the test set
y_pred = clf.predict(X_test_scaled)
 
 # Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)
 
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Confusion matrix:\n", conf_matrix)
print("Classification report:\n",class_report)
