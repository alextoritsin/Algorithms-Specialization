# Uses python3

def show_largest_number(numbers:list):
    answer = ''
    while len(numbers) > 1:
        max_digit = numbers[0]
        
        for i in range(1, len(numbers)):
            if len(max_digit) == len(numbers[i]):
                max_digit = max(max_digit, numbers[i])
            else:
                n0 = max_digit
                ni = numbers[i]
                max_digit = n0 if ni + n0 < n0 + ni else ni

        answer += max_digit
        numbers.remove(max_digit)
    
    answer += numbers[0]

    return answer

if __name__ == '__main__':
    n = int(input())
    numbers = [num for num in input().split()]
    print(show_largest_number(numbers))
    