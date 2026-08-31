def duplicate_encode(word):
    return "".join(["(" if word.lower().count(ch) == 1 else ")" for ch in word.lower()])


tests = [
    ("din", "((("),
    ("recede", "()()()"),
    ("Success", ")())())"),
    ("(( @", "))(("),
    ("", ""),
    ("a", "("),
    ("aa", "))"),
    ("Aa", "))"),
    ("abA", ")()"),
    ("aA bB", "))())"),
]

for inp, expected in tests:
    out = duplicate_encode(inp)
    print(f"{inp!r} -> {out!r} | expected {expected!r} | {'OK' if out == expected else 'FAIL'}")