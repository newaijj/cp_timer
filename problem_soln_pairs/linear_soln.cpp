#include <iostream>
#include <string>
#include <vector>

#define ll long long
#define vll vector<ll>

using namespace std;

int main(){
	ll t;
	cin>>t;
	vll v;

	for(ll i=0;i<t;i++){
		string s;
		cin>>s;
		cout<<s;
		v.push_back(i);
	}
	return 0;
}
