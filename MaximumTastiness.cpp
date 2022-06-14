#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while (t--){
        int n, maxi=0, prev;cin>>n;
        vector<ll> a(n);
        for (ll &i : a) cin >> i;
        sort(a.begin(), a.end());
        cout << a[n-1] + a[n-2]<< "\n"; 
    }
}