# Uses python3
import random

# def generate_input():
#     size = random.randint(0, 100)
#     n = random.randint(1, 4)
#     items = []
#     for i in range(n):
#         weight = random.randrange(0, 100, 10)
#         weight = weight if weight else 1
#         value = random.randrange(0, 100, 10)
#         if value > 0:
#             items.append((value / weight, value, weight))

#     items = sorted(items, key=lambda item: item[0], reverse=True)
#     return items, size

# def knapsack_lecture(items, size):
#     value = 0
#     for item in items:
#         if size == 0:
#             return round(value, 4)
#         amount = min(size, item[2])
#         value += item[0] * amount
#         size -= amount

#     return round(value, 4)
        

def knapsack(items, size):
    value = 0
    for item in items:
        if  item[2] < size:
            value += item[1]       
            size -= item[2]
        else:
            value += item[0] * size
            break
    
    return round(value, 4)

if __name__ == '__main__':
    n, size = map(int, input().split())
    if size == 0:
        print(0.000)
    else:
        items = []
        
        for i in range(n):
            v, w = map(int, input().split())
            if v > 0:
                items.append((v / w, v, w))

        value = knapsack(sorted(items, key=lambda item: item[0], reverse=True), size)

        print(value)