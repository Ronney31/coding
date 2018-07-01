/*

1
3*2
4*5*6
10*9*8*7

*/


#include<bits/stdc++.h>
using namespace std;

void fun(int a){
	int k=0;
	int j;
	
	for (int i=1; i<=a; i++){
		if(i%2!=0){
			for (j=k+1; j<k+i; j++){
				cout<<j<<"*";
			}
			cout<<j++<<endl;
			k=j;
		}
		else
		{
			k+=i-1;
			for (j=k; j>k-i+1; j--){
				cout<<j<<"*";
			}
			cout<<j<<endl;
		}
		
	}
	//return ;
	
}
int main()
{
	int a=4;
	fun(a);
	
	return 0;
}
