#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        int n, m;
        cin >> n >> m;
        if (!n && !m) {
            cout << 0<<"\n";
            continue;
            }
        int x = n*n + m*m;
        int ans = sqrt(x);

        if((ans * ans) == x) {
            cout << 1<<"\n";
            continue;
        } else {
            cout << 2<<"\n";
            continue;
        }
    }
}