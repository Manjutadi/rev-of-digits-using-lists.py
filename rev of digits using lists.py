def rev(n,data):

    def digits(i):
        d=0
        while i:
            r=i%10
            i=i//10
            d=d*10+r
        return d
    c=[]           
    for i in data:
        c.append(digits(i))
    return c
n=int(input())
data=list(map(int,input().split()))
r=rev(n,data)
print(*r)
