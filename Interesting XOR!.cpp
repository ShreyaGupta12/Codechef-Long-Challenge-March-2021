#include <bits/stdc++.h>
#include <iostream>
using namespace std;
typedef long long ll;
int main() {
	ll t,c,i;
	cin>>t;
	while(t--){
	    cin>>c;
	    ll temp,os=0,s=0;
	    temp=c;
	    i=0;
	    while(temp!=0){
	        if(temp%2==1) ++os;
	        ++s;
	        temp/=2;
	    }
	    int a[s],b[s];
	    ll v=s;
	    temp=c;
	    while(temp!=0){
	        if(temp%2==1){
	            if(os==1){
	                a[i]=1;
	                b[i]=0;
	            }
	            else{
	                a[i]=0;
	                b[i]=1;
	            }
	            os--;
	        }
	        else{
	            a[i]=1;
	            b[i]=1;
	        }
	        i++;
	        temp/=2;
	    }
	    ll p=1,n1=0,n2=0;
	    i=0;
	    while(i<v){
	        n1+=p*a[i];
	        n2+=p*b[i];
	        p*=2;
	        i++;
	    }
	    cout<<n1*n2<<endl;
	}
	return 0;
}
