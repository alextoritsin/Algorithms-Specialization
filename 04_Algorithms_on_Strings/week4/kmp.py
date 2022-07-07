# python3
import sys


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text 
    using Knuth-Morris-Pratt algorithm
    """
    if len(pattern) > len(text):
        return
    
    result = []
    string = pattern + '$' + text
    # compute prefix function of 'string'
    s = [0] * len(string)
    border = 0
    for i in range(1, len(string)):
        # decrease border while its not 0 and chars not equal
        while border > 0 and string[i] != string[border]:
            border = s[border - 1]
        # if char's equal: increase border length
        if string[i] == string[border]:
            border += 1
        else:
            # else assing border length to 0
            border = 0
        s[i] = border
        # check prefix func value and add to result if it equal to len patt
        if i > len(pattern) and s[i] == len(pattern):
            index = i - 2 * len(pattern)
            result.append(index)

    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    if result:
        print(" ".join(map(str, result)))
    else:
        print()

