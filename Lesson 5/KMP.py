def prefix (pattern):
    arr = []
    for i in range(len(pattern)):
        arr.append(pattern[0:i+1])
    return arr

def suffix (pattern):
    arr = []
    for i in range(len(pattern)):
        arr.append(pattern[i:len(pattern)])
    return arr

def Failure_function (pattern):
    P = pattern
    Fx = dict()
    for j in range(len(P)):
        if j == 0 :
            Fx[j] = -1
        else :
            Prefix = prefix(P[0:j])
            Suffix = suffix(P[1:j])
            arr = list(set(Prefix) & set(Suffix))
            if len(arr) == 0:
                Fx[j] = 0
            else :
                max_len = max([len(i) for i in arr])
                Fx[j] = max_len
    return Fx

def KMP (pattern,text):
    F = Failure_function(pattern)
    i = 0
    j = 0
    m = len(pattern)
    n = len(text)

    while i < n :
        while text[i] == pattern[j] :
            if j == m - 1 :
                print("Found pattern at index " + str(i-j))
                break
            elif i == n - 1 : break
            else:
                i+=1
                j+=1

        if text[i-1] == pattern[j-1] and j != m - 1:
            i = i - j

        if text[i] == pattern[j] and j == m - 1 :
            i = i - j
            j = 0

        i = i + j - F[j]
        j = F[j]
        if j == -1 : j = 0


if __name__ == '__main__':
    T = input('Enter text : ')
    P = input('Enter pattern to check if its in text or not : ')
    KMP(P,T)
