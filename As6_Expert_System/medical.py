class Symptom:
    def __init__(self,symptom):
        self.name=symptom
        self.state=False
class Disease:
    def __init__(self,disease,symptoms):
        self.name=disease
        self.symptoms=symptoms

class Expert:
    def __init__(self):
        self.symptoms=[]
        self.diseases=[]

    def add_symptom(self,name):
        symptom=Symptom(name)
        self.symptoms.append(symptom)
    def add_disease(self,disease,symptoms):
        disease= Disease(disease,symptoms)
        self.diseases.append(disease)
    
    def get_symptom_state(self,name):
        for symptom in self.symptoms:
            if symptom.name == name:
                return symptom.state
        return None

    def set_symptom_state(self,name,state):
        for symptom in self.symptoms:
            if symptom.name == name:
                symptom.state= state
                break
                
    def diagnose(self):
        possible_disease =[]
        for disease in self.diseases:
            matched_symp=0
            for symptom in disease.symptoms:
                if self.get_symptom_state(symptom):
                    print("matched_symp: ",matched_symp)
                    matched_symp+=1
            if matched_symp==len(disease.symptoms):
                print("possible onesss:",disease.name)
                possible_disease.append(disease.name)
        return possible_disease
    
    

expert = Expert()

# Define symptoms
expert.add_symptom("Fever")
expert.add_symptom("Cough")
expert.add_symptom("Headache")
expert.add_symptom("Fatigue")

# Define diseases
expert.add_disease("Common Cold", ["Fever", "Cough"])
expert.add_disease("Flu", ["Fever", "Cough", "Fatigue"])
expert.add_disease("Migraine", ["Headache"])
expert.add_disease("COVID-19", ["Fever", "Cough", "Fatigue", "Headache"])

# Taking User input for symptoms
for symptom in expert.symptoms:
    user_in = input(f"Does Patient have {symptom.name}(y/n): ")
    if user_in.lower()=='y':
        expert.set_symptom_state(symptom.name,True)

#performing diagnosis
possible = expert.diagnose()
possible.reverse()
print(possible)
