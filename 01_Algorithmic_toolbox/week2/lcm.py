# Uses python3

def lcm(a, b):
    if a == b:
        return a
    else:
        min_num, max_num = min(a, b), max(a, b)
        if max_num % min_num == 0:
            return max_num
            
        for i in range(2, min_num + 1):
            current = max_num * i
            if current % min_num == 0:
                return current


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

