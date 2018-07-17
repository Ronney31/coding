//counting the characters and displaying
#include<bits/stdc++.h>
using namespace std;

int main()
{
	string s;
	cin>>s;
	int i=0,tm=0,j=0;
	
	//initiallizing map
	map<char,int> mp;
	for(i=0; i<s.length(); i++){
		tm=1;
		for (j=i; j<s.length(); j++)
		{
			if(s[i]==s[j])
				tm+=1;
		}
		//inserting element to map
		mp.insert(pair<char,int>(s[i],tm));
	}
	
	//travelling 
	map<char,int>::iterator it = mp.begin();
	for (it; it!=mp.end(); ++it){
		cout<<it->first<<it->second;
	}
	
	return 0;
}
