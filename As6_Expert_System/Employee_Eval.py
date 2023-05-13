def Evaluation(employees):
    productivity = employees.productivity
    communication_skills = employees.communication_skills
    
    
    if productivity>=90 and communication_skills=="Excellent":
        return "Outstanding\n"
    elif productivity >=80 and communication_skills=="Good":
        return "Satisfactory\n"
    elif productivity<=80 and communication_skills=="Poor":
        return "Needs Improvement\n"
    elif productivity<70:
        return "Poor\n"
    elif productivity>80 and employees.Leadership_skills=="Exceptional":
        return "Execptional Leader\n"
    else:
        return "Evaluation Inconclusive\n"
    



class Employee:
    def __init__(self,productivity,communication_skills,Leadership_skills):
        self.productivity = productivity
        self.communication_skills = communication_skills
        self.Leadership_skills= Leadership_skills




def menu():
    productivity= int(input("\n\nEnter the Productivity rating (0-100): "))
    print("\n\n Excellent--> 1\n Good--> 2\n Poor--> 3\n To Skip this parameter--> 4\n\n")
    comm_choice= input("\nSelect the communication skills(choose from above): ")
    comm_skills="empty"
    if comm_choice=='1':
        comm_skills="Excellent"
    elif comm_choice=='2':
        comm_skills="Good"
    elif comm_choice=='3':
        comm_skills="Poor"
    elif comm_choice=='4':
        pass

    lead_skill=""
    excep_lead = input("\n\nLeadership skills(exeptional--> 1 ): ")
    if excep_lead=='1':
        lead_skill="Exceptional"


    employee1 = Employee(productivity,comm_skills,lead_skill)
    performance_rating= Evaluation(employee1)
    print("\n\nPerformance rating: "+performance_rating)


print("\nEmployee Evaluation System \n\n")
ans=input("Do you want to continue(y/n): ")
while(ans=='y' or ans=='Y'):
    menu()
    ans=input("Do you want to continue(y/n): ")
    
