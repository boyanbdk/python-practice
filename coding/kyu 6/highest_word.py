def score(w):
    return sum(ord(c) - ord('a') + 1 for c in w)

def high(x):
    bw = x.split()[0]
    bsc = score(bw)
    for w in x.split():
        sc = score(w)
        if sc > bsc:
            bsc = sc
            bw = w
    
    return bw
