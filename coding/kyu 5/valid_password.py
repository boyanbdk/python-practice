import re

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{6,}$'

tests = ["abcD1", "abcD1_", "abcdef1", "ABCDEF1", "aB3xyz", "12ABcd"]
for t in tests:
    ok = re.fullmatch(regex, t) is not None
    print(t, ok)
