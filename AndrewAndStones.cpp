#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        bool flag = true;
        int n, d, i;
        ll ans=0;
        vector<int> array;
        cin >> n;
        for (i=0; i<n; i++){
            cin >> d;
            array.push_back(d);
            if (i>0 && i<n-1 && d!=1 && flag){
                flag = false;
            }
        }
        if (n==3 && array[1]%2 || flag){
            cout << -1<<"\n";
            continue;
        }
        for (i=1; i<n-1; i++){
            ans += (array[i]+1)/2;
        }
        cout << ans<<"\n";
    }
}