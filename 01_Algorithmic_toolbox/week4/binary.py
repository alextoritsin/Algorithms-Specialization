# Uses python3

def get_number(array, number, l, r):
    
    while l <= r:
        mid = int((l + r) / 2)

        if array[mid] == number:
            return mid
         
        if number < array[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def search_numbers(array, numbers):
    result = []
    l, r = 0, len(array) - 1

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
    
    
    