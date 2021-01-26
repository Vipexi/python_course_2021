#! /usr/bin/python3

def simple_calculator(operation, number1, number2):
    operations = ("add","multiply")
    
    if not operation in operations:
        raise NameError("not a valid operation")
    else:
        
        if operation == "add": 
            answer = number1 + number2
        elif operation == "multiply":
            answer = number1 * number2
        else:
            answer = ""
        return answer

if __name__ == "__main__":
    print(simple_calculator("add",1,1))