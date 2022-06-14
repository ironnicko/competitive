#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >>t;
    while (t--){
        ll n, temp, sum=0; cin >> n;
        for (int i=0; i<n; i++){
            cin >> temp;
            sum += temp;
        }
        cout <<(sum%n ? 1 : 0)<<"\n";
    }
}