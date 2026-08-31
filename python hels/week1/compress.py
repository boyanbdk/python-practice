def compress(text):
    i = 0
    new_text = ""
    while i < len(text):
        count = 1
        while i+1 < len(text) and text[i] == text[i+1]:
            count += 1
            i += 1
        new_text += f"{text[i]}{count}"

        i += 1

    return new_text

print(compress("silas"))