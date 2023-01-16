#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t, temp=0;cin >> t;
    while (t--){
        int m; cin >> m;
        int arr[2][m];
        for (int i=0; i<2; i++){
            for (int j=0; j<m; j++){
                scanf("%i", &arr[i][j]);
                if (j > 0 && !i){
                    temp += arr[i][j];
                }
            }
        }
        ll sum =0;
        ll ans = 10e9;
        for (int i=0; i<m-1; i++){
            ans = min(ans, (temp > sum ? temp : sum));
            sum += arr[1][i];
            temp -= arr[0][i + 1];
        }
        ans = min(ans, (temp > sum ? temp : sum));
        cout << ans << "\n";
    }
}