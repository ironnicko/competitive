#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n; cin >> n;
        vector<ll> a(n);
        for (ll &i : a){
            cin >> i;
        }
        sort(a.begin(), a.end());
        ll diff= -a[n-1];
        for (ll i : a){
            diff += i;
        }
        diff = a[n-1] - diff;
        if (a[n-1]==0){
            cout << 0;
        }
        else if (diff <= 1){
            cout << 1;
        }
        else{
            cout << diff;
        }
        cout << "\n";
    }
}