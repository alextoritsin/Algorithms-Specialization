# python3
import sys


def PreprocessBWT(bwt:str):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
    """
    first_col = sorted(bwt)
    count = dict()
    starts = dict()
    for i, char in enumerate(bwt):
        # compute start of the char
        if first_col[i] not in starts:
            starts[first_col[i]] = i

        # compute count dict with arrays for every char
        for key in count:
            count[key][i + 1] = count[key][i]

        if char not in count:
            count[char] = [0] * (len(bwt) + 1)
            count[char][i + 1] = 1
        else:
            count[char][i + 1] = count[char][i] + 1


    return starts, count
    

def CountOccurrences(pattern, bwt, starts, count):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and count.
    """
    top = 0
    bottom = len(bwt) - 1
    pat_len = len(pattern)
    while top <= bottom:
        if pat_len:
            symbol = pattern[pat_len - 1]  
            pat_len -= 1
            if symbol not in count:
                return 0
            else:
                if count[symbol][bottom + 1] > 0:
                    top = starts[symbol] + count[symbol][top]
                    bottom = starts[symbol] + count[symbol][bottom + 1] - 1
                else:
                    return 0
        else:
            return bottom - top + 1
    return 0


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).  
    starts, count = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, count))
    print(' '.join(map(str, occurrence_counts)))
