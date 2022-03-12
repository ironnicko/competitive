#include <bits/stdc++.h>

typedef long long ll;

using namespace std;


int main(){
    int t;
    cin >> t;
    while (t--){
        ll n;
        cin >> n;
        if (n > 19){
            cout << "NO";
        } else{
            cout << "YES" << "\n";
            for (ll i=0; i < n; i++){
                cout << (ll)pow(3, i) << (i == n-1 ? "" : " ");
            }
        }
        cout << "\n";
    }
}