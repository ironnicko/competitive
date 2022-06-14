#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    while (t--){
        int n, temp, k; cin >> n >> k;
        bool flag = 1;
        set<int> result;
        for (int i=0; i<n; i++){
            cin >> temp;
            result.insert(temp);
        }
        for (int i : result){
            if (result.find(i-k) != result.end()){
                cout << "YES";
                flag = 0;
                break;
            }
        }
        cout << (flag ? "NO\n": "\n");
    }
}