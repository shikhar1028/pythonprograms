print("Welcome to This Calculator Program in Python")
a=int(input("Press 1 for Addition\n Press 2 for Subtraction\n  Press 3 for Multiplication\n   Press 4 for Division\n"))
while(a==1):
    b=int(input("Enter the first number:"))
    c=int(input("Enter the second number:"))
    d=b+c
    print("Sum of the numbers given is "+str(d))
    e=input("Want to continue????\n    Press y for Yes\n       Press n for No\n ")
    while(e=="y"):
        a=int(input("Press 1 for Addition\n Press 2 for Subtraction\n  Press 3 for Multiplication\n   Press 4 for Division\n"))
        break
    while(e=="n"):
        exit()
while(a==2):
    b=int(input("Enter the first number:"))
    c=int(input("Enter the second number:"))
    d=b-c
    print("Difference of the numbers given is "+str(d))
    e=input("Want to continue????\n    Press y for Yes\n       Press n for No\n ")
    while(e=="y"):
        a=int(input("Press 1 for Addition\n Press 2 for Subtraction\n  Press 3 for Multiplication\n   Press 4 for Division\n"))
        break
    while(e=="n"):
        exit()
while(a==3):
    b=int(input("Enter the first number:"))
    c=int(input("Enter the second number:"))
    d=b*c
    print("Multiplication of the numbers given is "+str(d))
    e=input("Want to continue????\n    Press y for Yes\n       Press n for No\n ")
    while(e=="y"):
        a=int(input("Press 1 for Addition\n Press 2 for Subtraction\n  Press 3 for Multiplication\n   Press 4 for Division\n"))
        break
    while(e=="n"):
        exit()
while(a==4):
    b=int(input("Enter the first number:"))
    c=int(input("Enter the second number:"))
    d=b/c
    print("Division of the numbers given is "+str(d))
    e=input("Want to continue????\n    Press y for Yes\n       Press n for No\n ")
    while(e=="y"):
        a=int(input("Press 1 for Addition\n Press 2 for Subtraction\n  Press 3 for Multiplication\n   Press 4 for Division\n"))
        break
    while(e=="n"):
        exit()
    
    
