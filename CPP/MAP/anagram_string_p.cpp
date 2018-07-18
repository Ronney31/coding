//anagram using map

#include<bits/stdc++.h>
using namespace std;

int func(string s,string p){
	map<char,int> mp;
	map<char,int> np;
	int i=0;
	for(i=0; i<s.length(); i++)
	{
		//mp.insert(pair<char,int>(s[i],0))
		mp[s[i]] ++;
	}
	for(i=0; i<p.length(); i++)
	{
		np[s[i]] ++;
	}
	int m;
	//m=(s.length()<p.length() ? s.length() : p.length());
	map<char,int>::iterator it=mp.begin();
	map<char,int>::iterator ti=np.begin();
	try{
	for(it,ti; it!=mp.end(),ti!=np.end(); ++it,++ti){
		if((it->first!=ti->first) || (it->second!=ti->second)){
			return 0;
		}
	}
	return 1;
	/*
	map<char,int>::iterator it=mp.begin();
	for(it; it!=mp.end(); ++it){
		cout<<it->first<<" "<<it->second<<endl;
	}*/
	}
	catch (exception e){
		cout<<"Error"<<endl;
	}
}
int main(){
	string s,p;
	cin>>s>>p;
	
	int res=0;
	res = func(s,p);
	if(res == 1)
		cout<<"Yes, string is anagram"<<endl;
	else
		cout<<"No, string is not anagram"<<endl;
	
	
	
	
	return 0;
}
