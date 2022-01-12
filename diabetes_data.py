from seaborn.matrix import heatmap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

DIABETES_DATA_FILE = "diabetes.csv"
TARGET = "Outcome"


class diabetes_data:

    def __init__(self):
        self.data = pd.read_csv(DIABETES_DATA_FILE).dropna()
        del self.data['Pregnancies']
        self.features_list = list(self.data.columns)

    def get_data(self):
        return self.data

    def get_features(self):
        return self.features_list

    def get_heatmap(self):
        heatmap(self.data.corr(), annot=True)
        plt.show()

    def plot_outcomes(self):
        plt.style.use("ggplot")
        self.data["Outcome"].value_counts().plot.bar(
            title='Outcome', rot=0)
        plt.show()

    def plot_ages(self):
        plt.style.use("ggplot")
        list_ages = []

        for a in self.data["Age"]:
            for e in range(0, 100, 10):
                if a >= e and a <= (e+9):
                    label = "%d-%d" % (e, (e+9))
                    list_ages.append(label)
        pd.DataFrame(list_ages).value_counts().plot.bar(
            title='Ages', rot=0)
        plt.show()

    def plot_BMI(self):
        plt.style.use("ggplot")
        list_BMI = []

        for bmi in self.data["BMI"]:
            for b in range(0,70,10):
                if bmi >= b and b <=(bmi+9):
                    label = "%d-%d"%(b,(b+9))
                    list_BMI.append(label)
        pd.DataFrame(list_BMI).value_counts().plot.bar(
            title='BMI', rot=0)
        plt.show()

    def get_training_data(self):

        y = self.data[[TARGET]].values
        x = self.data.drop(TARGET, axis='columns').values

        return x, y
    
    def get_medium_values_diabetes(self):

        medium_values = {}
        positives = self.data[self.data['Outcome'] == 1]
        
        medium_values['BloodPressure'] = positives['BloodPressure'].mean()
        medium_values['SkinThickness'] = positives['SkinThickness'].mean()
        medium_values['Insulin'] = positives['Insulin'].mean()
        medium_values['BMI'] = positives['BMI'].mean()

        return medium_values