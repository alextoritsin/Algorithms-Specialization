# python3
import sys


def sort_single_chars(text):
    """
    Sorts single chars of string `text`
    with counting sort
    """
    char = dict()
    order = [0] * len(text)

    # count the numb of occur of each char
    for c in text:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
            
    count = [0] * len(char)
    # assign value for every letter inside `count` arr
    # and compute relations btw char and indexes
    for i, c in enumerate(sorted(char)):
        count[i] = char[c]
        char[c] = i
    
    # compute partial sums
    for j in range(1, len(char)):
        count[j] += count[j - 1]
    # form order array with sorted chars
    for i in range(len(text) - 1, -1, -1):
        c = char[text[i]]
        count[c] -= 1
        order[count[c]] = i

    return order


def compute_char_classes(text, order):
    """
    Compute equivalent classes of
    single chars of string `text`
    using order array
    """
    cls = [0] * len(text)
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            cls[order[i]] = cls[order[i - 1]] + 1
        else:
            cls[order[i]] = cls[order[i - 1]]

    return cls 


def sort_doubled(text, L, order, cls):
    """
    Given the partial cyclic shifts of string `text`
    of length L sorts partial cyclic shifts
    of length 2*L
    """
    n = len(text)
    # `count` array for diff equivalent classes
    count = [0] * n
    new_order = [0] * n
    # count the number of diff eq. classes
    for i in range(n):
        count[cls[i]] += 1
    for j in range(1, n):
        count[j] = count[j] + count[j - 1]
    # go thought arr of double cyclic shift sorted by sec halfes
    for i in range(n - 1, -1, -1):
        start = (order[i] - L + n) % n
        # get the class of the shift with this index
        cl = cls[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    
    return new_order


def update_classes(new_order, cls, L):
    """
    Updates classes of double cyclic shifts
    """
    n = len(new_order)
    new_class = [0] * n
    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = (cur + L) % n, (prev + L) % n
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]

    return new_class


def build_suffix_array_naive(text):
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


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value order[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sort_single_chars(text)
    cls = compute_char_classes(text, order)
    L = 1
    while L < len(text):
        order = sort_doubled(text, L, order, cls)
        cls = update_classes(order, cls, L)
        L = 2 * L

    return order


def find_occurrences(text, patterns):
    """
    Finds all occurences of pattern in text
    using suffix array by finding in binary
    search two pointers of starting and ending
    indexes of array
    """
    occs = set()
    order = build_suffix_array(text)
    for pattern in patterns:
        # find position in suf array,
        # when suffix no less than pattern
        min_index = 0
        max_index = len(text)
        while max_index - min_index != 1:
            mid_index = (min_index + max_index) // 2
            t = text[order[mid_index]:]
            if pattern > t:
                min_index = mid_index
            else:
                max_index = mid_index

        start = max_index
        # find the next position in suf array, when prefix of suffix
        # more than pattern
        min_index = start - 1
        max_index = len(text)
        while max_index - min_index != 1:
            mid_index = (min_index + max_index) // 2
            i = order[mid_index]
            prefix = text[i:min(i + len(pattern), len(text))]
            if prefix > pattern:
                max_index = mid_index
            else:
                min_index = mid_index
        
        end = max_index
                
        for i in range(start, end):
            occs.add(order[i])

    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    text += '$'
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))