#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int t;
    cin >> t;
    while (t--){
        ll n;
        cin >> n;
        vector<ll> A(n);
        for (ll &i : A){
            cin >> i;
        }
        sort(A.begin(), A.end());
        ll ib=1, ir=n-1;
        ll sb = A[0] + A[1], sr = A[n-1];
        while ((ib <= ir) && (sb >= sr)){
            ib += 1;
            ir -= 1;
            sb += A[ib];
            sr += A[ir];
        }
        cout << (ir >= ib ? "YES" : "NO") <<"\n";
    }
}