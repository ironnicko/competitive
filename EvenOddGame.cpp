#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ll t;
    cin >> t;
    while (t--){
        ll n, d, i;
        cin >> n;
        ll alice = 0;
        ll bob = 0;
        vector<ll> A;
        for (i=0; i<n; i++){
            cin >> d;
            A.push_back(d);
        }
        sort(A.begin(), A.end());
        for (i=0; i<n; i++){
            if (i%2==0 && A[n-i-1]%2==0){
                alice += A[n-i-1];
            }
            else if (i%2==1 && A[n-i-1]%2==1){
                bob += A[n-i-1];
            }
            A.pop_back();
        }
        if (alice > bob){
            cout << "Alice"<< "\n";
        }
        else if (alice == bob){
            cout << "Tie"<< "\n";
        }
        else{
            cout << "Bob" << "\n";
        }
    }
}