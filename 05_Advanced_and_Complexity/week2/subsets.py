def combination_indicies(n, k, j=0, stack=[]):   
    if len(stack) == k:            
        yield set(stack)
        return
        
    for i in range(j, n):
        stack.append(i)
        for x in combination_indicies(n, k, i + 1, stack):            
            yield x
        stack.pop()  


for st in combination_indicies(5, 3):
    print(st)