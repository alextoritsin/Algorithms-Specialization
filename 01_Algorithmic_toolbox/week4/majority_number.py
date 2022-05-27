# Uses python3


def get_majority_number(array):
    numbers = {}
    for num in array:
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1

    for key in numbers:
        if numbers[key] > len(array) / 2:
            return 1
    
    return 0



if __name__ == '__main__':

    n = int(input())
    array = [int(i) for i in input().split()]

    print(get_majority_number(array))
    
    
    