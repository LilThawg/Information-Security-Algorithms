#Alogorithm 01
def Multiprecision_addition(a,b) :
    e = 0
    c = ['']*len(a)
    for i in range(len(a),0,-1):
        c[i-1] = (a[i-1]+b[i-1]+e) %  2**8
        if a[i-1]+b[i-1]+e  >= 2**8 :
            e = 1
        else : e = 0
    return (e,c)
  
def check_add (a,b,c) :
    t = len(a)
    A = 0
    B = 0
    C = 0
    for i in range(t):
        A += a[i] * pow(2, (t - 1 - i) * 8)
        B += b[i] * pow(2, (t - 1 - i) * 8)
        C += c[i] * pow(2, (t - 1 - i) * 8)
    if (A+B)%(2**(8*t)) == C :
        return True
    else : return False
    
if __name__ == '__main__':
    a = [57,169,36,27]
    b = [0,98,34,62]
    print(Multiprecision_addition(a, b))
    c = Multiprecision_addition(a,b)[1]
    print(check_add(a,b,c))
