# uses python3

max_value = float('-inf')
stack = []
aux = []

def stack_with_max(cmd:str):

    get_cmd = cmd.split()
    if get_cmd[0] == 'push':
        num = int(get_cmd[1])
        stack.append(num)    
        if len(aux):
            last = aux[-1]
            aux.append(max(num, last))
        else:
            aux.append(num)
    elif get_cmd[0] == 'pop':
        stack.pop()
        aux.pop()

    elif get_cmd[0] == 'max':
        print(aux[-1])

if __name__ == '__main__':
    q = int(input())
    
    for i in range(q):
        stack_with_max(input())
    