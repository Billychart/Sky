#grading system..

from lib2to3.pgen2 import grammar


grade = {"35" :"F",
"45" : "D",
"55" : "C",
"65" : "B",
"75" : "A" }

Score = int(input(f"what is your score? >  "))


  
if Score >= 75: 
        print(f"Congratulations!!! you got A and passed")

elif Score >= 65 and Score < 75:
        print(f"you got B and passed")

elif Score >= 55 and Score < 65 :
        print(f"you got C and passed")

elif Score >= 45 and Score < 55:
      print(f"you got D and performed poor")
    
elif Score >= 0 and Score < 44:
        print("you failed with a F")
