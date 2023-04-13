# from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# import random
# import pandas as pd
#
# # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.data.gz"
# data = pd.read_csv('covtype.data', header=None)
# data = data.iloc[:1000, :]
#
# columns = [
#     'Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology',
#     'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
#     'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
#     'Horizontal_Distance_To_Fire_Points'
# ]
# wilderness_areas = [f'Wilderness_Area_{i}' for i in range(1, 5)]
# soil_types = [f'Soil_Type_{i}' for i in range(1, 41)]
# columns.extend(wilderness_areas)
# columns.extend(soil_types)
# columns.append('Cover_Type')
# data.columns = columns
#
# X = data.drop('Cover_Type', axis=1)
# y = data['Cover_Type']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)
#
# random_forest = RandomForestClassifier()
# random_forest.fit(X_train, y_train)
# forest_pred = random_forest.predict(X_test)
# forest_acc = accuracy_score(y_test, forest_pred)
# print(f"Accuracy Score - Random Forest = {forest_acc}")
#
# logistic_reg = LogisticRegression()
# logistic_reg.fit(X_train, y_train)
# logistic_reg_pred = logistic_reg.predict(X_test)
# logistic_reg_acc = accuracy_score(y_test, logistic_reg_pred)
# print(f"Accuracy Score - Logistic Regression = {logistic_reg_acc}")
#
# random_index = np.random.randint(0, len(X_test))
# sample = X_test[random_index]
# # sample = X_train[0]
# sample = sample.reshape(1, -1)
# sample = scaler.transform(sample)
# predicted_cover_type = random_forest.predict(sample)
# print(f"Predicted 'Cover_type' = {predicted_cover_type[0]}")

# idx = random.randint(0, len(X_test) - 1)
# sample = X_test[idx]
# sample = sample.reshape(1, -1)
# sample = scaler.transform(sample)
# predicted_cover_type = random_forest.predict(sample)
# print(f"Value: {y_test.iloc[idx]}, Predicted: {predicted_cover_type[0]}")


from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import random
import pandas as pd


class CoverTypeClassifier:
    def __init__(self, data_file_path, num_rows=1000):
        self.data = pd.read_csv(data_file_path, header=None)
        self.data = self.data.iloc[:num_rows, :]

        columns = [
            'Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology',
            'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
            'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
            'Horizontal_Distance_To_Fire_Points'
        ]
        wilderness_areas = [f'Wilderness_Area_{i}' for i in range(1, 5)]
        soil_types = [f'Soil_Type_{i}' for i in range(1, 41)]
        columns.extend(wilderness_areas)
        columns.extend(soil_types)
        columns.append('Cover_Type')
        self.data.columns = columns

        self.X = self.data.drop('Cover_Type', axis=1)
        self.y = self.data['Cover_Type']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42)

        self.scaler = StandardScaler()
        self.scaler.fit(self.X_train)
        self.X_train = self.scaler.transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

        self.random_forest = RandomForestClassifier()
        self.random_forest.fit(self.X_train, self.y_train)
        self.logistic_reg = LogisticRegression()
        self.logistic_reg.fit(self.X_train, self.y_train)

    def get_random_forest_accuracy(self):
        forest_pred = self.random_forest.predict(self.X_test)
        forest_acc = accuracy_score(self.y_test, forest_pred)
        return forest_acc

    def get_logistic_regression_accuracy(self):
        logistic_reg_pred = self.logistic_reg.predict(self.X_test)
        logistic_reg_acc = accuracy_score(self.y_test, logistic_reg_pred)
        return logistic_reg_acc

    def predict_cover_type(self, sample):
        sample = sample.reshape(1, -1)
        sample = self.scaler.transform(sample)
        predicted_cover_type = self.random_forest.predict(sample)
        return predicted_cover_type[0]


# classifier = CoverTypeClassifier(data_file_path='covtype.data')
# print("Random Forest Accuracy:", classifier.get_random_forest_accuracy())
# print("Logistic Regression Accuracy:", classifier.get_logistic_regression_accuracy())
# sample = np.array(
#     [2596, 51, 3, 258, 0, 510, 221, 232, 148, 6279,
#     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# predicted_cover_type = classifier.predict_cover_type(sample)
# print(f"Predicted 'Cover_type' = {predicted_cover_type}")