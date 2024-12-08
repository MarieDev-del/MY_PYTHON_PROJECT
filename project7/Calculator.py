first_operation=int(input("Enter first number: "))
operators=["+","-","/","*"]
for i in operators:
    print(i)
continue_operation=False
while not continue_operation:
    chosen_operator=(input("Choose an operator: "))
    second_operation=int(input("Enter next number: "))
    def add(first_operation,second_operation):
        if chosen_operator=="+":
            c=first_operation+second_operation
            return(f"{first_operation}+{second_operation}={c}")
        elif chosen_operator=="-":
            c=first_operation-second_operation
            return(f"{first_operation}-{second_operation}={c}")
        elif chosen_operator=="/":
            c=first_operation/second_operation
            return(f"{first_operation}/{second_operation}={c}")
        else:
            c=first_operation*second_operation
            return(f"{first_operation}*{second_operation}={c}")      
    A= add(first_operation,second_operation)
    print(A)
    should_continue=input("Enter 'yes' to continue with the last input or 'no' to exist: ").lower()
    if should_continue=='yes':
        first_operation=A
    else:
        continue_operation=False
        print("Byes")    
    
    
