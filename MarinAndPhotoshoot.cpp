#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while (t--){
        int n, count=0;cin>>n;
        string s;cin >> s;
        for (int i=0; i<n-1; i++){
            if (s[i] == '1'){
                if (0 < i < n-1){
                    if (s[i-1] == s[i+1] && s[i+1] == '0') count ++;
                }
            }
            if (s[i] == s[i+1] && s[i] == '0') count += 2;
        }
        cout << count<< "\n";
    }
}