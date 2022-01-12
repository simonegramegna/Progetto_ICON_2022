from owlready2 import *
import os

class diabetes_ontology:
    def __init__(self):
        self.ontology = get_ontology(os.path.basename("diabetes_symptoms.owl")).load()
        self.dict_symptoms = {}

    def get_symptoms_descriptions(self):
        dict_symptoms_onto = {}

        for i in self.ontology.individuals():
            dict_symptoms_onto[str(i)] = i.descrizione_sintomo

        for k in dict_symptoms_onto.keys():

            k1 = k
            k1 = k1.replace("diabetes_symptoms.istanza_","")
            self.dict_symptoms[k1] = dict_symptoms_onto[k]


    def print_symptoms(self):

        i = 1
        dict_nums_symptoms = {}
        dict_nums_keys = {}

        for k in self.dict_symptoms.keys():

            print("Sintomo [%d]: Nome: %s"%(i,k))
            dict_nums_symptoms[i] = self.dict_symptoms[k]
            dict_nums_keys[i] = k
            i = i + 1

        return dict_nums_symptoms, dict_nums_keys

