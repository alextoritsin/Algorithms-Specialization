# uses python3


from collections import deque


def poly_hash(s, x, p):
    hash = 0
    for i in range(len(s)):
        hash = (hash + ord(s[i]) * x ** i) % p
    
    return hash
    

def calc_hashes(hashes, pat, text, x, p):
    last_pat = text[len(text) - len(pat):]
    # calc hash of the last pattern
    hashes[-1] = poly_hash(last_pat, x, p)

    # calc multiplier
    y = 1
    for i in range(1, len(pat) + 1):
        y = (y * x) % p

    # calc remain hashes
    for i in range(len(hashes) - 2, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + len(pat)])) % p
    

def rabin_karp(pat, text):
    hashes = [0] * (len(text) - len(pat) + 1)
    p = 10000000007
    x = 1
    res = []
    pat_hash = poly_hash(pat, x, p)
    calc_hashes(hashes, pat, text, x, p)
    text_as_deque = deque(text[:len(pat)])
    pat_as_deque = deque(pat)

    for i in range(len(hashes)):
        if pat_hash == hashes[i]:
            if text_as_deque == pat_as_deque:
                res.append(i)
        if i < len(hashes) - 1:
            text_as_deque.popleft()    
            text_as_deque.append(text[i + len(pat)])
            
            
            
        # if pat_hash != hashes[i]:
            
        #     continue
        # else:
        #     # if text[i:i + len(pat)] == pat:
            

    return " ".join([str(i) for i in res])


if __name__ == '__main__':
    pat = input()
    text = input()
    
    print(rabin_karp(pat, text))