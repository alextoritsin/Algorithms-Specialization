# python3

def find_two_max_product(array):
    max1, max2 = -1, -2
    
    for i in range(len(array)):
        if array[i] > max1:
            max2, max1 = max1, array[i]
        elif array[i] > max2:
            max2 = array[i]
            
    return max1 * max2

if __name__ == '__main__':
    n = int(input())
    array = [int(elem) for elem in input().split()]
    print(find_two_max_product(array))

