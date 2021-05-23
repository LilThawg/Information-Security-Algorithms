def last_occurrence(pattern,text):
    Lx = dict()
    alphabet = ''.join(set(text))
    for letter in alphabet:
        Lx[letter] = pattern.rfind(letter)
    return Lx

def Boyer_Moore(pattern,text):

    Lx = last_occurrence(pattern,text)

    m = len(pattern)
    n = len(text)
    i = m - 1
    j = m - 1

    while i < n :
        if text[i] == pattern[j] :
            if j == 0:
                return i
            else :
                i = i - 1
                j = j - 1
        else :
            i = i + m - min(j, 1+Lx[text[i]])
            j = m - 1

    return -1

if __name__ == '__main__':
    T = input('Enter text : ')
    P = input('Enter pattern to check if its in text or not : ')
    if Boyer_Moore(P,T) == -1:
        print('NO MATCH !')
    else :
        print('HAVE A MATCH AT INDEX {}'.format(Boyer_Moore(P,T)))








