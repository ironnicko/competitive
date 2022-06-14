#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while (t--){
        int even=0, odd=0, odd_elems=0, even_elems=0, n, temp;
        cin >> n;
        for(int i=0; i<n; i++){
            cin >> temp;
            if (temp % 2){
                odd ++;
                odd_elems += abs(odd - even);
            } else{
                even ++;
                even_elems += abs(odd - even);
            }
        }
        if (abs(even - odd) > 1) cout << -1;
        else{
            if (even > odd) cout << odd_elems;
            else if (odd > even) cout << even_elems;
            else cout << min(odd_elems, even_elems);
        }
        cout << "\n";
    }
}