#  https://www.codechef.com/DEC20B/problems/EVENPSUM
# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    if x%2==0:
        ee=x//2
        oo=x//2
    else:
        ee=x//2
        oo=ee+1
    if y%2==0:
        ee1=y//2
        oo1=y//2
    else:
        ee1=y//2
        oo1=ee1+1
    r=ee*ee1+oo1*oo
    print(r)