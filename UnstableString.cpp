#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        string s;
        cin >> s;
        vector<vector<int> > list(2, vector<int>(2, -1));
        ll ans=0;
        int j, p, i;
        for (i=0; i<s.size(); i++){
            j = i-1;
            p = i & 1;
            if (s[i] != '1') j = min(j, max(list[0][p^1], list[1][p]));
            if (s[i] != '0') j = min(j, max(list[0][p], list[1][p^1]));
            ans += i-j;
            if (s[i] != '?') list[s[i] - '0'][p] = i;
        }
        cout << ans << "\n";
    }
}