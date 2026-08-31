def duplicate_count(text):
    text = text.lower()
    text_unique = set(text)
    cnt = 0

    for i in text_unique:
        if text.count(i) > 1:
            cnt += 1
        
    return cnt

if __name__ == "__main__":
    print(duplicate_count("aabBcde"))  # очакваш 2
    print(duplicate_count("Indivisibility"))  # очакваш 1
    print(duplicate_count("abcde"))  # очакваш 0
