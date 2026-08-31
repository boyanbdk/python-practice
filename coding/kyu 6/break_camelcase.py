def solution(s):
    camel_s = []
    for i in range(len(s)):
        if s[i].isupper():
            camel_s.append(" ")
        camel_s.append(s[i])

    return "".join(camel_s)