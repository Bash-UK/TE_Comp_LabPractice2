def get_college(marks):
    colleges = {
        'collegeA': {'cet': 90, 'hsc': 85, 'jeee': 90},
        'collegeB': {'cet': 80, 'hsc': 90, 'jeee': 85},
        'collegeC': {'cet': 85, 'hsc': 80, 'jeee': 90},
        'collegeD': {'cet': 75, 'hsc': 85, 'jeee': 80},
        'collegeE': {'cet': 85, 'hsc': 85, 'jeee': 85}
    }
    
    suitable_colleges = []
    for college, criteria in colleges.items():
        if marks['cet'] >= criteria['cet'] and marks['hsc'] >= criteria['hsc'] and marks['jeee'] >= criteria['jeee']:
            suitable_colleges.append(college)
    
    return suitable_colleges

def chatbot():
    print("Welcome to the College Selection Chatbot!")
    print("Please enter your marks obtained in the respective exams.")
    
    marks = {}
    marks['cet'] = float(input("CET marks: "))
    marks['hsc'] = float(input("HSC marks: "))
    marks['jeee'] = float(input("JEEE marks: "))
    
    suitable_colleges = get_college(marks)
    
    if len(suitable_colleges) > 0:
        print("Based on your marks, the suitable college(s) for you are:")
        for college in suitable_colleges:
            print(college)
    else:
        print("Sorry, based on your marks, there are no suitable colleges for you.")
    
    print("Thank you for using the College Selection Chatbot!")

# Run the chatbot
while True:
    chatbot()
