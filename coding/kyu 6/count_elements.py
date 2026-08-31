def count(s):
    return {ch: s.count(ch) for ch in set(s)}
