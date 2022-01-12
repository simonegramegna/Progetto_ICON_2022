from models import *
from numpy import linspace
import matplotlib.pyplot as plt
from diabetes_data import diabetes_data


def get_linspace(start: int, end: int, step: int):

    linspace_vect = []

    for i in range(start, end, step):
        linspace_vect.append(i)

    return linspace_vect


def metrics_graph_lr(data: diabetes_data, test_size: float):

    iterations_vect = linspace(0, 2000, 100)
    precision_vect = []
    recall_vect = []
    f1_score_vect = []
    accurancy_vect = []

    a, graph_lr = plt.subplots(4, 1)
    a.tight_layout(pad=3.0)

    i = 0
    while i < len(iterations_vect):

        model_i = diabetes_logistic_regression(
            data, iterations_vect[i], test_size)

        model_i.predict()
        accurancy_vect.append(model_i.get_metric("Accurancy"))
        precision_vect.append(model_i.get_metric("Precision"))
        recall_vect.append(model_i.get_metric("Recall"))
        f1_score_vect.append(model_i.get_metric("F1_precision"))

        i = i + 1

    graph_lr[0].plot(iterations_vect, accurancy_vect)
    graph_lr[0].set_title("Accurancy - Logistic Regression")

    graph_lr[1].plot(iterations_vect, precision_vect)
    graph_lr[1].set_title("Precision - Logistic Regression")

    graph_lr[2].plot(iterations_vect, recall_vect)
    graph_lr[2].set_title("Recall - Logistic Regression")

    graph_lr[3].plot(iterations_vect, f1_score_vect)
    graph_lr[3].set_title("F1_Precision - Logistic Regression")

    plt.show()


def metrics_graph_dt(data: diabetes_data, test_size: float):

    iterations_vect = linspace(0, 200, 5)
    precision_vect = []
    recall_vect = []
    f1_score_vect = []
    accurancy_vect = []

    a, graph_lr = plt.subplots(2, 2)
    a.tight_layout(pad=4.0)

    i = 0
    while i < len(iterations_vect):

        model_i = diabetes_decision_tree(data, iterations_vect[i], test_size)

        model_i.predict()
        accurancy_vect.append(model_i.get_metric("Accurancy"))
        precision_vect.append(model_i.get_metric("Precision"))
        recall_vect.append(model_i.get_metric("Recall"))
        f1_score_vect.append(model_i.get_metric("F1_precision"))

        i = i + 1

    graph_lr[0, 0].plot(iterations_vect, accurancy_vect)
    graph_lr[0, 0].set_title("Accurancy - Decision Tree")

    graph_lr[0, 1].plot(iterations_vect, precision_vect)
    graph_lr[0, 1].set_title("Precision - Decision Tree")

    graph_lr[1, 0].plot(iterations_vect, recall_vect)
    graph_lr[1, 0].set_title("Recall - Decision Tree")

    graph_lr[1, 1].plot(iterations_vect, f1_score_vect)
    graph_lr[1, 1].set_title("F1_Precision - Decision Tree")
    plt.show()


def metrics_graph_knn(data: diabetes_data, test_size: float):

    iterations_vect = get_linspace(1, 50, 1)
    precision_vect = []
    recall_vect = []
    f1_score_vect = []
    accurancy_vect = []

    a, graph_lr = plt.subplots(2, 2)
    a.tight_layout(pad=4.0)

    i = 0
    while i < len(iterations_vect):

        model_i = diabetes_knn(data, test_size, iterations_vect[i])

        model_i.predict()
        accurancy_vect.append(model_i.get_metric("Accurancy"))
        precision_vect.append(model_i.get_metric("Precision"))
        recall_vect.append(model_i.get_metric("Recall"))
        f1_score_vect.append(model_i.get_metric("F1_precision"))

        i = i + 1

    graph_lr[0, 0].plot(iterations_vect, accurancy_vect)
    graph_lr[0, 0].set_title("Accurancy - KNN")

    graph_lr[0, 1].plot(iterations_vect, precision_vect)
    graph_lr[0, 1].set_title("Precision - KNN")

    graph_lr[1, 0].plot(iterations_vect, recall_vect)
    graph_lr[1, 0].set_title("Recall - KNN")

    graph_lr[1, 1].plot(iterations_vect, f1_score_vect)
    graph_lr[1, 1].set_title("F1_Precision - KNN")
    plt.show()


def comparison_metrics_models(data: diabetes_data, test_size: float):

    model_1 = diabetes_logistic_regression(data, 100, test_size)
    model_1.predict()

    model_2 = diabetes_decision_tree(data, 50, test_size)
    model_2.predict()

    model_3 = diabetes_knn(data, test_size, 21)
    model_3.predict()

    a, graph_lr = plt.subplots(2, 2)
    a.tight_layout(pad=4.0)

    precision_data_dict = {"Logistic_Regression": model_1.get_metric("Precision"), "Decision_Tree": model_2.get_metric(
        "Precision"), "K-Nearest-Neighbor": model_3.get_metric("Precision")}

    recall_data_dict = {"Logistic_Regression": model_1.get_metric("Recall"), "Decision_Tree": model_2.get_metric(
        "Recall"), "K-Nearest-Neighbor": model_3.get_metric("Recall")}

    f1_data_dict = {"Logistic_Regression": model_1.get_metric("F1_precision"), "Decision_Tree": model_2.get_metric(
        "F1_precision"), "K-Nearest-Neighbor": model_3.get_metric("F1_precision")}

    accurancy_data_dict = {"Logistic_Regression": model_1.get_metric("Accurancy"), "Decision_Tree": model_2.get_metric(
        "Accurancy"), "K-Nearest-Neighbor": model_3.get_metric("Accurancy")}

    models_names = list(precision_data_dict.keys())

    models_precision_data = list(precision_data_dict.values())
    models_recall_data = list(recall_data_dict.values())
    models_f1_data = list(f1_data_dict.values())
    models_accurancy_data = list(accurancy_data_dict.values())

    graph_lr[0, 0].bar(models_names, models_precision_data, color="red")
    graph_lr[0, 0].set_title("Precision")

    graph_lr[0, 1].bar(models_names, models_recall_data, color="green")
    graph_lr[0, 1].set_title("Recall")

    graph_lr[1, 0].bar(models_names, models_f1_data, color="purple")
    graph_lr[1, 0].set_title("F1-precision")

    graph_lr[1, 1].bar(models_names, models_accurancy_data, color="blue")
    graph_lr[1, 1].set_title("Accurancy")

    plt.show()
