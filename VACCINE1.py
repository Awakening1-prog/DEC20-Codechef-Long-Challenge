#  https://www.codechef.com/DEC20B/problems/VACCINE1



d11,v11,d22,v22,p=map(int,input().split())

ress=min(d11,d22)-1
if d11==d22:
    x=v11+v22
    if p%x==0:
        print((p//x)+ress)
    else:
        print((p//x)+1+ress)
else:
    r=0
    rd=abs(d11-d22)
    fl11=fl22=fl33=fl44=0
    if d11<d22:
        r=rd*v11
        if r>=p:
            if p%v11==0:
                fl11=1
            else:
                fl22=1
        else:
            r=r
    else:
        r=rd*v22
        if r>=p:
            if r%v22==0:
                fl33=1
            else:
                fl44=1
        else:
            r=r
    while r<p:
        if r>=p:
            break
        r+=v11+v22
        rd+=1
    if fl11==1:
        print(p//v11+ress)
    elif fl22==1:
        print(p//v11+ress+1)
    elif fl33==1:
        print(p//v22+ress)
    elif fl44==1:
        print(p//v22+ress+1)
    else:
        print(rd+ress)