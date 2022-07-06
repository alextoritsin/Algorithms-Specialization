# python3
import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    n = len(text)
    result = [0] * n
    result[0] = (0, text)
    for i in range(n - 1):
        t = result[i][1]
        t = t[-1] + t[:n - 1]
        result[i + 1] = (n - 1 - i, t)

    result.sort(key=lambda x: x[1])
    return " ".join([str(elem[0]) for elem in result])


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(build_suffix_array(text))
