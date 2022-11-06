#quiz has questions and answers.

import random


quiz = [ {"Question" : "how many elements are in the periodic table?",
"a" : "150",
"b" : "200",
"c" : "118",
"d" : "250",
 "Answer" : "c"} , 

{"Question" : "what company was originally called 'cadabra'?",
"a" : "Facebook",
"b" : "Apple inc.",
"c" : "Blackrock",
"d" : "Amazon",
 "Answer" : "d"},

{"Question" : "what planet has the most moons?",
"a" : "jupiter",
"b" : "saturn",
"c" : "mars",
"d" : "earth",
 "Answer" : "b"},

{"Question" : "who is the current president of Nigeria?",
"a": "M. buhari",
"b" : "Peter Obi",
"c" : "Atiku A.",
"d" : "Tinibu(jagaban)",
 "Answer" : "a"},

{"Question" : "who founded facebook?",
"a" : "Steve Jobs",
"b" : "Mikel Obi",
"c" : "Mark Zuckerberg",
"d" : "Buhari",
 "Answer" : "c"} ]


quizunmber : list = len(quiz)
correctAnswer : int = 0


number = 0
random.shuffle(quiz)
correction: list = []

for n in quiz:
    A = n["Question"]
    number += 1
   
    print(f'Question {number} : {A}')
    print(f'a: {n["a"]}')
    print(f'b: {n["b"]}')
    print(f'c: {n["c"]}')
    print(f'd: {n["d"]}')
    inputAns = (input(f'answer >' )).lower()

    if inputAns == "a" or inputAns == "b" or inputAns == "c" or inputAns == "d":


        if n["Answer"] == inputAns:
            correctAnswer = correctAnswer + 1
            print(correctAnswer)

            print('\n answer is correct \n')
        else: 
            print("\n incorrect answer \n")

            correction.append({"question": n["Question"],
            "Answer" : n[ n["Answer"]]})

    else:
        print("wrong input")
    
print(f'you got {correctAnswer} out of {quizunmber}')

if correction:
        print("correction") if len(correction) <= 1 else print("correction")
        print(correction)
