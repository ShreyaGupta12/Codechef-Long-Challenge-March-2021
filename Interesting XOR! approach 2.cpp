//Another Solution Can be:
#include <bits/stdc++.h>
#define int long long int
using namespace std;


int pow(int a,int b){
    int rs = 1;
    for(int i = 1 ; i <=b ; i++){
        rs = rs * a;
    }
    return rs;
}

int32_t main() {
	// your code goes here
    	int t;
    	cin>>t;
    	while(t){
        	int c; 
        	cin>>c;
        	int d = log2(c)+1;
        	int n = c;
        	int rs ;
        	int up_bound = pow(2,d-1);
        	int A = up_bound-1;
        	int cnt = 0 ;
        	int B = 0;
        	while(n!=0){
        	    if((n&1)==1){
        	        cnt++;
        	    }else{
        	        B = B+pow(2,cnt);
        	        cnt++;
        	    }
        	    n = n>>1;
        	}
        	B = B + up_bound ;
        	rs = A*B;
        	
        	cout<<rs<<endl;
    	
    	    t--;
	    }
	return 0;
}
