#  https://www.codechef.com/DEC20B/problems/VACCINE2/

# cook your dish here
t=int(input())
for i in range(t):
    aa,bb=map(int,input().split())
    l=list(int(x) for x in input().split())
    ao=0
    r=0
    ai=0
    for i in range(len(l)):
        if l[i]>=80 or l[i]<=9:
            ao+=1
        else:
            ai+=1
    if ao%bb==0:
        r+=ao//bb
    else:
        r+=ao//bb+1
    if ai%bb==0:
        r+=ai//bb
    else:
        r+=ai//bb+1
    print(r)