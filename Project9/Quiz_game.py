print('****************************************************')
print("Welcome To My Quiz Game")
Quiz_questions = [
    {"Text":"The ability of one class to acquire methods and attributes of another class is called_____","Answer":"D"},
    {"Text":"Which of the following is a type of inheritance?","Answer":"D"},
    {"Text":"What type of inheritance has multiple subclasses to a single superclass?","Answer":"D"},
    {"Text":"What is the depth of multilevel inheritance in python?","Answer":"C"},
    {"Text":"What does MRO stand for?","Answer":"A"}
]
Options = [
    ["A.Inheritance","B.Abstraction","C.Polymorphism","D.Objects"],
    ["A.Single","B.Double","C.Multiple","D.both A and C"],
    ["A.Multiple Inheritance","B.Multilevel Inheritance","C.Hierarchical Inheritance","D.None of the above"],
    ["A.Two level","B.Three level","C.Any leve","D.one of the above"],
    ["A.Main Resolution Order","B.Method Recursion Object","C.Main Resoluton Order","D.Method Resolution Object"]
]
score = 0
def Guess_answer(Guess_input,correct_answer):
    if Guess_input==correct_answer:
        return True
    else:
        return False
for i in range(len(Quiz_questions)):
    print('****************************************************')
    print(Quiz_questions[i]['Text'])
    for j in Options[i]:
        print(j)
    Guess_input = input("Enter your answer(A/B/C/D):").upper() 
    Is_correct=Guess_answer(Guess_input,Quiz_questions[i]["Answer"])
    if Is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
    print(f"Your current score is {score}/{i}")
print(f"You have given {score} correct answers")
print(f"Your score is {(score/len(Quiz_questions))*100}")
    