from constraint import *

class laboratory_csp(Problem):

    def __init__(self,lab_name: str, solver=None):
        super().__init__(solver=solver)
        self.lab_name = lab_name
        self.days = self.addVariable("day",["lunedi","martedi","mercoledi","giovedi","venerdi","sabato"])
        self.hours = self.addVariable("hours",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
        self.availability = None

    def get_availability(self):

        self.availability = sorted(self.getSolutions(), key=lambda h: h['hours'])
        first_turn = None
        last_turn = None

        if len(self.availability) > 0:

            print("Disponibilita' dello studio\n")
            i = 0
            first_turn = i

            while i < len(self.availability):
                
                print("Turno [%d], Giorno: %s, Orario: %d"%(i,self.availability[i]['day'],self.availability[i]['hours']))
                i = i + 1
            
            last_turn = i-1
            print("\n")
               
        else:
            print("Non c'è disponibilita'")

        return first_turn, last_turn
    
    def print_single_availability(self, index):

        if index >= 0 and index < len(self.availability):
            print("Turno selezionato: [%d], Giorno: %s, Orario: %d\n\n"%(index,self.availability[index]['day'],self.availability[index]['hours']))
