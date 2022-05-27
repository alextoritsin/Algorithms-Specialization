# Uses python3

def get_number(array, number, l, r):
    
    while r - l != 1:
        mid = int((l + r) / 2)

        if number <= array[mid]:
            r = mid
        else:
            l = mid

    if r == len(array) or array[r] != number:
        return -1
    else:
        return r


def search_numbers(array, numbers):
    result = []
    l, r = -1, len(array)

    for num in numbers:
        index = get_number(array, num, l, r)
        result.append(str(index))
                
    return " ".join(result)


if __name__ == '__main__':

    n = int(input())
    array = [int(i) for i in input().split()]
    m = input()
    numbers = [int(j) for j in input().split()]

    print(search_numbers(array, numbers))
    
    
    