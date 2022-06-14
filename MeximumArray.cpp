#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    while (t--){
        int n, mex=0; cin >> n;
        vector<int> q(n), ans;
        for(int &i : q) cin >> i;
        map<int, int> rem;
        for (int i : q) rem[i]++;
        set<int> c;
        for (int i=0; i<n; i++){
            c.insert(q[i]);
            while (c.find(mex) != c.end()) mex++;
            if (rem[mex] == 0){
                ans.push_back(mex);
                c.clear();
                mex = 0;
            }
            rem[q[i]] -= 1;
        }
        cout << ans.size() << '\n';
        for (int i : ans) cout << i <<" ";
        cout << '\n';
    }
    return 0;
}