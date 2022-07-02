# python3
import sys

def BWT(text):
    """Finds Burrows-Wheeler transform of the text"""
    n = len(text)
    matrix = [0] * n
    matrix[0] = text
    for i in range(n - 1):
        matrix[i + 1] = matrix[i][-1] + matrix[i][:n - 1]

    matrix.sort()

    return "".join([s[-1] for s in matrix])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))