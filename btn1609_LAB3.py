
#Benjamin Niccum
#1002111609
#03/24/24

def calculate(line):
    operators = set(['+', '-', '*', '/'])
    stack = []
    
    for token in line:                   #Goes through every token in line
        if token not in operators:       #Token is an integer
            stack.append(int(token))     #Throw it on the stack
        else:                            #Found first operator
            #pop off last two integers, perform function, place result on the stack
            b = stack.pop()               
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
    
    if len(stack) == 0:
        return None
    else:
        return stack[0]

# Main program
file = "input_RPN.txt"                   #Hardcoded
with open(file, 'r') as f:
    for line in f:                        #Sends input one line at a time
        line = line.replace("\n","")      #Removes Linebreak from the end of the line
        line = line.replace(" ","")       #Removes Spaces
        result = calculate(line)          
        print("Result:", result)