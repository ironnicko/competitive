#include<bits/stdc++.h>
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,n,i,j,ce=0;
    cin>>t;
    while(t--){

        string operated_on;
        cin>>operated_on;


        n = operated_on.size();

        ll sum = 0;
        for(i=0; i<n; i++){
            sum+=int(operated_on[i]-'a');
            sum++;
        }
        if(!(n&1)){
            cout<<"Alice "<<sum<<"\n";

        }else{
            ll sum1 = sum - int(operated_on[0]-'a') - 1;
            ll vint = sum - int(operated_on[n-1]-'a') - 1;
            ll autm = max(sum1, vint);
            ll rem = sum-autm;
            if(autm>rem){
                cout<<"Alice "<<autm-rem<<"\n";
            }else{
                cout<<"Bob "<<rem-autm<<"\n";
            }
        }
    }
}

