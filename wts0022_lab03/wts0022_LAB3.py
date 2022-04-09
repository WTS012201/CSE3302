#  William Sigala
#  CSE 3302
#  Lab 3
#  ID# 1001730022
import os

def calculate(expr):
    stack, symbols = [], expr.strip().split()
    for sym in symbols:
        if sym == '+':      #   If symbol on top of stack is operator, then pop the next two numbers on the stack and apply the operation
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)
        elif sym == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(a - b)
        elif sym == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(a * b)
        elif sym == '/':    
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:               # Else the symbol is a character so put it on the stack
            stack.append(float(sym))
    return stack[0]

def main():
    input_file = os.path.abspath("input_RPN.txt")
    try:
        with open(input_file, 'r') as f:
            RPN_expr = f.readlines()
    except:
        print("No input file named input_RPN.txt in current working directory")
    for expr in RPN_expr:
        print(calculate(expr))

if __name__ == "__main__":
    main()