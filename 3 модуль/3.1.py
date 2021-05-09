def get_hash(a, b, c, d):
    res = 0
    for j in range(0, b):
        res=(res*d+ord(a[j]))%c
    return res


def rabin_karp(a, b, c, d):
    hb=get_hash(b, len(b), c, d)
    ha=get_hash(a, len(b), c, d)
    db=1
    l=[]
    for j in range (len(b)):
        db=(db*d)%c
    for j in range(len(a)-len(b)+1):
        if hb==ha:
            l.append(j)
        if j+len(b)<len(a):
            ha=(ha*d-ord(a[j])*db+ord(a[j+len(b)]))%c

    print(" ".join(map(str, l)))
def main():
    a=input()
    b=input()
    c=1e9+7
    d=26
    rabin_karp(a,b,c,d)
main()