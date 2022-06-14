#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--){
        int n, k, limit;
        ll count=0, temp;
        cin >> n >> k;
        vector<int> pos, neg;
        for (int i=0; i<n; i++){
            cin >> temp;
            if (temp < 0){
                neg.push_back(abs(temp));
            }else{
                pos.push_back(temp);
            }
        }
        reverse(pos.begin(), pos.end());
        for (int i=0; i<neg.size(); i+=k){
            count += neg[i];
        }
        for (int i=0; i<pos.size(); i+=k){
            count += pos[i];
        }
        count *= 2;
        if (!neg.size()) count -= pos[0];
        else if (!pos.size()) count -= neg[0];
        else count -= max(pos[0], neg[0]);
        cout << count <<"\n";
    }
}