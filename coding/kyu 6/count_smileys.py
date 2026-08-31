"""def mouth_eyes_ok():
    (w[0] == ":" or w[0] == ";")
                     and (w[-1] == ")" or w[-1] == "D")"""

def count_smileys(arr):
    if len(arr) == 0:
        return 0
    else:
        return len([w for w in arr if (len(w) == 3 and (w[0] == ":" or w[0] == ";")
                     and (w[-1] == ")" or w[-1] == "D") and (w[1] == "-" or w[1] == "~"))
                     or
                     len(w) == 2 and (w[0] == ":" or w[0] == ";")
                     and (w[-1] == ")" or w[-1] == "D")])