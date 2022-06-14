#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m, flag=0;
    cin >> n >> m;
    if (n > m){
        cout << "NO";
        return 0;
    } else flag =1;
    if (flag){
        for (int i = n+1; i <= m; i++) {
            if (i == 1 || i == 0)
                continue;
            flag = 1;
            for (int j = 2; j <= i / 2; ++j) {
                if (i % j == 0) {
                    flag = 0;
                    break;
                }
            }
            if (flag){
            cout << (i == m ?"YES" : "NO");
            return 0;
                }
        }
    }
    if (!flag)
    cout << "NO";
}