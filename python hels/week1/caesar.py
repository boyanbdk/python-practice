def caesar(text, shift):

    azbuka = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    i = 0

    while i < len(text):
        if text[i] not in azbuka:
            new_text += text[i]
        else:
            new_text += azbuka[(azbuka.find(text[i]) + shift) % 26]

        i += 1

    return new_text

print(caesar("xyz", 3))
