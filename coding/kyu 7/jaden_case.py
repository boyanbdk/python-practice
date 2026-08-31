def to_jaden_case(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:].lower()
    return " ".join(words)

print(to_jaden_case("a good day"))