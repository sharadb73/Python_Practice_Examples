from numpy import sqrt

def isprime(pnum):
    i = 2
    while pnum > i:
        if pnum % i == 0:
            return i
        i += 1
    return pnum

def primefactor(pnum):
    divnum = []
    fpnum = []
    ans = 0
    if pnum % 2 == 0:
        pass
    for i in range(3, sqrt(pnum).astype(int), 2):
        if pnum % i == 0:
            divnum.append(i)
            num = isprime(i)
            if i == num:
                fpnum.append(i)

    print(divnum)
    print(fpnum)
    ans = fpnum[-1]
    return ans

num = primefactor(600851475143)
# num = primefactor(13195)
# num = isprime(6)
print(num)