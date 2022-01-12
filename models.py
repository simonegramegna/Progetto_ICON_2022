from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             confusion_matrix, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import matplotlib.pyplot as plt
from typing import Final
from diabetes_data import diabetes_data

class diabetes_model:

    def __init__(self, model, x, y, scores_dict: dict, test_size: float):

        default_test_size: Final = 0.5

        if self.__check_test_size(test_size) == False:
            test_size = default_test_size

        self.model = model
        self.x = x
        self.y = y
        self.scores = scores_dict
        self.test_size = test_size
        self.target = "Outcome"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_metric(self, score_label: str):

        score_val = None

        if score_label in self.scores.keys():
            score_val = self.scores[score_label]

        return score_val

    def print_metrics(self):
        for s in self.scores.keys():
            print("%s : %.3f" % (str(s), self.scores[s]))

    def __check_test_size(self, test_size: float):

        valid = False

        if test_size > 0 and test_size < 1:
            valid = True

        return valid


class diabetes_logistic_regression(diabetes_model):

    def __init__(self, data: diabetes_data, iterations: int, test_size: float):
        default_iterations: Final = 100

        if iterations < 1:
            iterations = default_iterations

        x, y = data.get_training_data()
        diabetes_model.__init__(self, LogisticRegression(
            max_iter=iterations), x, y, {}, test_size)

        self.test_size = test_size

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.x, self.y, test_size=self.test_size)
        self.y_predicted = None

    def predict(self):
        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.fit_transform(self.x_test)

        self.model.fit(self.x_train, self.y_train.ravel())

        self.y_predicted = self.model.predict(self.x_test)

        # calcolo e memorizzo le metriche di valutazione sul modello
        self.scores["Accurancy"] = accuracy_score(
            self.y_test, self.y_predicted)
        self.scores["Precision"] = precision_score(
            self.y_test, self.y_predicted)
        self.scores["Recall"] = recall_score(self.y_test, self.y_predicted)
        self.scores["F1_precision"] = f1_score(self.y_test, self.y_predicted)
    
    def get_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_predicted)
        disp_matrix = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
        disp_matrix.plot()
        plt.grid(False)
        plt.title("Confusion matrix Logistic Regression")
        plt.show()


class diabetes_decision_tree(diabetes_model):

    def __init__(self, data: diabetes_data, max_d: int, test_size: float):
        default_tree_depth: Final = 10

        if max_d < 1:
            max_d = default_tree_depth

        x, y = data.get_training_data()

        diabetes_model.__init__(self, tree.DecisionTreeClassifier(
            max_depth=max_d), x, y, {}, test_size)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.x, self.y, test_size=self.test_size)
        self.y_predicted = None

    def predict(self):
        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.fit_transform(self.x_test)

        self.model.fit(self.x_train, self.y_train.ravel())
        self.y_predicted = self.model.predict(self.x_test)

        # calcolo e memorizzo le metriche di valutazione sul modello
        self.scores["Accurancy"] = accuracy_score(
            self.y_test, self.y_predicted)
        self.scores["Precision"] = precision_score(
            self.y_test, self.y_predicted)
        self.scores["Recall"] = recall_score(self.y_test, self.y_predicted)
        self.scores["F1_precision"] = f1_score(self.y_test, self.y_predicted)

    def get_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_predicted)
        disp_matrix = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
        disp_matrix.plot()
        plt.grid(False)
        plt.title("Confusion matrix Decision Tree")
        plt.show()

class diabetes_knn(diabetes_model):

    def __init__(self, data: diabetes_data, test_size: float, neighbors: int):
        
        x, y = data.get_training_data()
        self.neighbors = neighbors
        diabetes_model.__init__(self, KNeighborsClassifier(
            n_neighbors=self.neighbors), x, y, {}, test_size)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.x, self.y, test_size=self.test_size)

        self.y_predicted = None
    
    def predict(self):

        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.fit_transform(self.x_test)

        self.model.fit(self.x_train, self.y_train.ravel())
        self.y_predicted = self.model.predict(self.x_test)

        # calcolo e memorizzo le metriche di valutazione sul modello
        self.scores["Accurancy"] = accuracy_score(
            self.y_test, self.y_predicted)
        self.scores["Precision"] = precision_score(
            self.y_test, self.y_predicted)
        self.scores["Recall"] = recall_score(self.y_test, self.y_predicted)
        self.scores["F1_precision"] = f1_score(self.y_test, self.y_predicted)

    def get_confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_predicted)
        disp_matrix = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
        disp_matrix.plot()
        plt.grid(False)
        plt.title("Confusion matrix K-Nearest-Neighbor")
        plt.show()
