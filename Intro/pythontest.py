print "We are going to do a calculation.\nPlease enter two didgets and an operator. \n"

def getResult(input_1, op, input_2):
    if op == "+":
        print(int(input_1) + int(input_2))
    elif op == "-":
        print(int(input_1) - int(input_2))
    elif op == "/":
        print(float(input_1) / float(input_2))
    elif op == "*":
        print(int(input_1) * int(input_2))
    elif op == "**":
        print(int(input_1) ** int(input_2))
    else:
        print("Invalide operator given. Use / * - +", op)


d1 = raw_input("Please enter the first didget: ")
op = raw_input("Please enter desired operator: ")
d2 = raw_input("Please enter the second didget: ")


getResult(d1, op, d2)
