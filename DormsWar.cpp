#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin>> t;
    while (t--){
        int n, k, last = -1, last_pos = 0;cin>>n;
        string s;cin >> s >> k;
        char temp;
        set<char> c; for (int i=0; i<k; i++){
            cin >> temp;
            c.insert(temp);
        }
        for (int i=0; i<n; i++){
            if (c.find(s[i]) != c.end()){
                if (last_pos != -1) last = max(last, i-last_pos);
                last_pos = i;
            }
        }
        cout << (last != -1 ? last : last_pos) << "\n";
    }
}