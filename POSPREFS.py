#   https://www.codechef.com/DEC20B/problems/POSPREFS



# cook your dish here
t1=int(input())
for i in range(t1):
    n,k=map(int,input().split())
    if n==k:
        arr=[i for i in range(1,k+1)]
        print(*arr)
    else:
        x=abs(n-k)
        arr=[i for i in range(1,n+1)]
        i=0
        while x>0 and i<len(arr):
            arr[i]=-1*arr[i]
            i+=2
            x-=1
        if x>0:
            for i in range(len(arr)-1,-1,-1):
                if arr[i]>0:
                    arr[i]=-arr[i]
                    x-=1
                if x==0:
                    break
            print(*arr)
        else:
            print(*arr)