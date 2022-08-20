#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while (t--){
        int n, l, r, k, score=0;
        cin >> n >> l >> r >> k;
        vector<int> choc(n);
        for (int i=0; i < n; i++){
            cin >> choc[i];
        }
        for (int i : choc){
            if (i >= l && i <= r && k >= i){
                k -= i;
                score+=1;
            }
        }
        cout << score<< "\n";
    }
}