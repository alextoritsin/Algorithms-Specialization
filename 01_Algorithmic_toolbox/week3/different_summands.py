# Uses python3

def get_prizes_list(n):
    prizes = []
    prize = 1

    while n != 0:

        if n - prize > prize:
            prizes.append(prize)    
            n -= prize        
            prize += 1
        else:
            prizes.append(n)
            n = 0
    return [str(i) for i in prizes]

if __name__ == '__main__':
    n = int(input())
    prizes = get_prizes_list(n)
    print(len(prizes))
    print(" ".join(prizes))
    