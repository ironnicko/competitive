#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int n, one=0, con=0, prev;cin >> n;
    vector<int> a(n);
    for (int &i : a) cin >> i;
    sort(a.begin(), a.end());
    prev = a[0];
    for (int i : a){
        if (i==1) one =1;
        if (prev + 1 == i) con = 1;
        prev = i;
    }
    cout << (one && con ? "NO\n" : "YES\n");
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while (t--)solve();
    return 0;
}