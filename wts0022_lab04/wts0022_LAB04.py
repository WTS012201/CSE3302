# William Sigala
# ID: 1001730022
# Due Date: April 26, 2022
# Windows 10, Python 3.10.1

import os

def block(input, output='0 ', index=-1, depth=0):
    if depth < 0:                                           #   Check if there is a closing bracket before opening bracket
        print("expected ‘{’ before ‘}’")
        exit()

    index += 1
    if index >= len(input) and depth > 0:                   #   Check if EOF at current position
        print("expected ‘}’ but found EOF")
        exit()
    elif index >= len(input):
        return

    output += input[index]
    index, output = ignore(input, output, index, depth)     #   Check if we need to ignore brackets at current position

    if index >= len(input) and depth > 0:                   #   Check if EOF after ignore
        print("expected ‘}’ but found EOF")
        exit()
    elif index >= len(input):
        return

    if input[index] == '\n' or input[index] == '\0':        #   Print annotated line
        print(output, end='')
        output = f"{depth} "
    if input[index] == '{':                                 #   If open bracket, then increase annotated output depth and go into next block
        output = replace(output, depth + 1)
        block(input, output, index, depth + 1)
    elif input[index] == '}':                               #   If close bracket, then decrease annotated output depth and go into next block
        block(input, output, index, depth - 1)
    else:
        block(input, output, index, depth)

def replace(output, depth):                                 #   Used to change the annotated output depth if a bracket is found in the line
    index = 0
    while output[index] != ' ':
        index += 1
    return f"{depth}{output[index:]}"

def ignore(input, output, index, depth):
    if input[index] == "\"":
        index, output = ignore1(input, output, index, depth)
    if index + 1 < len(input):
        if input[index] + input[index + 1] == "//":
            index, output = ignore2(input, output, index, depth)
    if index + 1 < len(input):
        if input[index] + input[index + 1] == "/*":
            index, output = ignore3(input, output, index, depth)
    if index - 1 >= len(input):
        index -= 1
    return index, output

#   ignore for " "
def ignore1(input, output, index, depth):
    index += 1
    if index >= len(input):
        print("expected ‘\"’ but found EOF")
        exit()
    output += input[index]
    if input[index] == '\n' or input[index] == '\0':
        print(output, end='')
        output = f"{depth} "
    if input[index] == "\"":
        return index, output
    return ignore1(input, output, index, depth)

#   ignore for //
def ignore2(input, output, index, depth):
    index += 1
    if index >= len(input):
        return index, output
    output += input[index]
    if input[index] == '\n' or input[index] == '\0':
        print(output, end='')
        output = f"{depth} "
    if input[index] == "\n":
        return index + 1, output
    return ignore2(input, output, index, depth)

#   ignore for /* */
def ignore3(input, output, index, depth):
    index += 1
    if index + 1 >= len(input):
        print("expected ‘*/’ but found EOF")
        exit()
    output += input[index]
    if input[index] == '\n' or input[index] == '\0':
        print(output, end='')
        output = f"{depth} "
    if input[index] + input[index + 1] == "*/":
        return index, output
    return ignore3(input, output, index, depth)

def main():
    input_file = os.path.abspath("input.txt")
    try:
        with open(input_file, 'r') as f:
            input = f.read()
    except:
        print("No input file named input.txt in current working directory")
        exit()
    block(input + '\0')

if __name__ == "__main__":
    main()