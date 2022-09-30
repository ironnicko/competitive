#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
        int n; cin >> n;
        n%=1000001;
        string s; cin >> s;

        vector<int> togetoff;
        for(int i=0; i<n; i++){
            if (s[i] == '0')togetoff.push_back(i+1);
        }

        int N = togetoff.size();
        if (N == 0){
            cout << 0<<endl;
            return;
        }
        vector<int> zeroes(n+1, 0);
        ll finalANS = 0;
        for (int i=0; i<N; i++){
            int middle=1;
            while (binary_search(togetoff.begin(), togetoff.end(), middle*togetoff[i])){
                if (!zeroes[middle*togetoff[i]]){ finalANS += togetoff[i];}
                zeroes[middle*togetoff[i]]=1;
                middle++;
            }
        }
        cout << finalANS<<endl;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;

    while(t--){
        solve();
    }
    return 0;
}