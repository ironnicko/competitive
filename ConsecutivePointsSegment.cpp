#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while(t--){
        int n, temp, prev=0, diff = 0;cin >> n;
        for (int i=0; i<n; i++){
            cin >> temp;
            diff += (!prev ? 0 : temp - prev);
            prev = temp;
        }
        cout << (diff > n+1 ? "NO" : "YES") << '\n';
    }   
}