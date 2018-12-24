#https://www.codechef.com/submit/IGCDMNKY
'''
t=int(input())
for i in range(t):
    h,m,n=map(int,input().strip().split())
    jum = 0.0
    if jum == h :
        print (jum)
    else:
        i = 0
        while(i<=h):
            if i+m == h :
                jum+=1
                break
            elif i+m > h:
                jum += (m-(i+m-h))/m
                break
            i=i+m-n
            jum+=1
    print ("%.2f"%jum)
'''
t=int(input())
while (t):
    h,m,n=map(int,input().strip().split())
    dist = 0
    jump = 0.0
    while(1):
        dist+=m
        if(dist == h):
            jump+=1
            break
        elif(dist > h):
            jump+=(m-(dist-h))/m
            break
        jump+=1
        dist-=n
    print ("%.2f"%jump)
    t-=1

    
'''
######c++ code
#include <iostream>
#include <boost/format.hpp>
using namespace std;
int main()
{
	 long int h=0;
	 int m,n,t=0;
	 cin>>t;
	 while(t--)
	 {
        cin>>h>>m>>n;
        float jump = 0.0;
        int dist = 0 ;
        while(1)
        {
            dist+=m;
            if(dist == h)
            {
                jump+=1;
                break;
            }
            else if ( dist > h)
            {
                jump+=float((m-(dist-h)))/float (m );
                break;
            }
        	jump+=1;
        	dist-=n;
         }
        cout<<boost::format("%.2f") %jump<<endl;
	}
	return 0;	    
}
'''
