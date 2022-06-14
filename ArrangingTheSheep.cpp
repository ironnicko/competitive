#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    while (t--){
        int n, b=0, dots=0; cin >> n;
        ll ans =0;
        char string[n];
        for (int i=0; i<n; i++) {
            cin >> string[i];
            if (string[i] == '*') dots++;
        }
        for (char i : string){
            if (i == '*') b++;
            else ans += min(b, dots - b); 
        }
        cout << ans << '\n';
    }

}