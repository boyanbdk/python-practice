import string

def is_pangram(st):
    alphabet = string.ascii_lowercase
    st = st.lower()

    letters = set(st)
    
    for i in alphabet:
        if not (i in letters):
            return False
    
    return True