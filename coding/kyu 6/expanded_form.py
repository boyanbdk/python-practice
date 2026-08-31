def expanded_form(num):
    num = str(num)
    parts = []
    for i, ch in enumerate(num):
        if ch != "0":
            zeros = len(num) - i - 1
            parts.append(ch + "0"*zeros)
    
    return " + ".join(parts)