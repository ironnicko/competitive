#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while(t--){
        int n, c=0;cin >> n;
        string s; cin >> s;
        vector<int> ans(n, 8);
        for (int i=0; i<n; i++){
            if (s[i] == 'a'){
                if (i+1 < n && s[i+1] == 'a'){
                    ans[i] = 2;
                    break;
                } else if (i + 2 < n && s[i+2] == 'a') ans[i] = 3;
                else if (i+3 < n && s[i+1] != s[i+2] && s[i+3] == 'a')ans[i] = 4;
                else if (i+6 < n && s[i+1] == s[i+2] && s[i+3] == 'a' && s[i+6] == 'a' && s[i+4] == s[i+5]){
                    if (s[i+1] == s[i+4]) continue;
                    ans[i] = 7;
                }
            }
        }
        sort(ans.begin(), ans.end());
        cout << (ans[0] != 8 ? ans[0] : -1) << '\n';
    }
}