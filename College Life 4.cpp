#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
typedef long long ll;
ll findcase(ll n,ll e,ll h,ll a,ll b,ll c,ll ans){
    ll temp,r=1;
    if (n<=0) return 0;
    if ((n<=e) && (n<=h))
        ans=min(n*c,ans);
    if (3*n<=h) 
        ans=min(n*b,ans);
    if (2*n<=e)
        ans=min(n*a,ans);
    if (e/2>=1 && e/2>=((3*n-h+2)/3)){//chocomilk and omlette
    if ((a-b)<0){
        temp=min(n-1,e/2);
        ans=min(ans,(a-b)*temp+n*b);
    }
    else{
        temp=max(r,(3*n-h+2)/3);
        ans=min(ans,(a-b)*temp+n*b);
    }
    }
    if ((h-n)/2>=1 && (h-n)/2>=(n-e)){//choco milk and cake
    if ((b-c)<0){
        temp=min(n-1,(h-n)/2);
        ans=min(ans,(b-c)*temp+n*c);
    }
        else{
            temp=max(r,n-e);
            ans=min(ans,(b-c)*temp+n*c);
        }
    }
    if (e-n>=1 && e-n >=n-h){
        if((a-c)<0){
            temp=min(n-1,e-n);
            ans=min(ans,(a-c)*temp+n*c);
        }
        else{
            temp=max(r,n-h);
           ans=min(ans,(a-c)*temp+n*c); 
        }
    }//omlette and cake
    if (e>=3 && h>=4 && n>=3) ans=min(a+b+c+findcase(n-3,e-3,h-4,a,b,c,ans),ans);
    return ans;}
int main() {
	int t,n,e,h,a,b,c,i,j,k;
	cin>>t;
	while(t--){
	    cin>>n>>e>>h>>a>>b>>c;
	    ll ans=1e15;
	    ans=findcase(n,e,h,a,b,c,ans);
    if (ans==1e15) cout<<-1<<endl;
    else cout<<ans<<endl;
	}
	return 0;
}
