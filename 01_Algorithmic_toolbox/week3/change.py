# Uses python3

def change(money):
    my_change = [10, 5, 1]
    counter = 0
    for amount in my_change:
        while money - amount >= 0:
            money -= amount
            counter += 1
    
    return counter


if __name__ == '__main__':
    m = int(input())
    print(change(m))

