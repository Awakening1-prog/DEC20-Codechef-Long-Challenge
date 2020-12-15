//https://www.codechef.com/DEC20B/problems/HXOR




#include <stdio.h>
#include<math.h>
int main() {

    long long int t;
    scanf("%lld",&t);
    while(t--)
    {
    long long int n,x,z,f;
    scanf("%lld",&n);
    scanf("%lld",&x);
    long long int arr[100000000];
    for(long long int i=0;i<n;i++)
    {
        scanf("%lld",&arr[i]);
    }
     int i=0;
    long long k=x;
    for(long long int k=x;k>0 && i<n-1;k--)
    {
        f=0;
        long long int p=log(arr[i])/log(2);
        long long int pw=1<<p;
        arr[i]=arr[i]^pw;
        for(long long int j=i+1;j<n;j++)
        {
            if((arr[j]^pw)<arr[j])
            {
                arr[j]=arr[j]^pw;
                f=1;
                break;
            }
        }
		if(f==0)
		{
  			arr[n-1]=arr[n-1]^pw;  
		}
		while(arr[i]<=0)
		{
    		i+=1;
		}  
	 z=k+1;
    }
	if(z>0)
	{
    	if((n<3) && (z%2>0))
   		 {
    	    arr[n-2]=arr[n-2]^1;
        	arr[n-1]=arr[n-1]^1;
   		 }
	}

   	for(long long int i=0;i<n;i++)
  {
      printf("%lld ",arr[i]);
  }
}
 }