#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int countSC(int N)
{
    int res = (int)sqrt(N) + (int)cbrt(N)
              - (int)(sqrt(cbrt(N)));
 
    return res;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while (t--){
        ll n;cin >> n;
        cout << countSC(n) << "\n";

    }
}