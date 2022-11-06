
#"1" = "addition"
#"2" = "subtraction"
#"3" = "multiplication"
#"4" = "division"

print("select your operation >")
print("1 > Addition")
print("2 > Subtraction")
print("3 > Multiplication")
print("4 > Division")

Operation = input()

if Operation == "1":
    num1 = input("Enter first value :")
    num2 = input("Enter second value :")
    answer = int(num1) + int(num2)
    print(f"the answer is = {answer}")
elif Operation == "2":
    num1 = input("Enter first value :")
    num2 = input("Enter second value :")
    answer = int(num1) - int(num2)
    print(f"the answer is = {answer}")
elif Operation == "3":
    num1 = input("Enter first value :")
    num2 = input("Enter second value :")
    answer = int(num1) * int(num2)
    print(f"the answer is = {answer}")
elif Operation == "4":
    num1 = input("Enter first value :")
    num2 = input("Enter second value :")
    answer = int(num1) / int(num2)
    print(f"the answer is = {answer}")