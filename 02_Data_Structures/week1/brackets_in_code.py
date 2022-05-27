# uses python3

def calc_brackets(s:str):
    stack = []
    push = {'(', '{', '['}
    pop = {')', '}', ']'}
    for i, char in enumerate(s):
        if char in push:
            stack.append((char, i + 1))
        elif char in pop:
            if len(stack):
                last = stack.pop()[0]
                if (char == ')' and last != '(' or 
                    char == '}' and last != '{' or 
                    char == ']' and last != '['):
                    return i + 1
            else:
                return i + 1

    if len(stack) == 0:
        return 'Success'                 
    else:
        return stack[0][1]


if __name__ == '__main__':
    string = input()    
    
    print(calc_brackets(string))