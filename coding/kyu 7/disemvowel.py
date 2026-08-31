def disemvowel(string_):
    vowels = set('aouieAOUIE')
    return "".join(ch for ch in string_ if ch not in vowels)