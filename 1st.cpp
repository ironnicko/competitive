#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int d, s, n; cin >> n;
    bool ok=1;
    cin >> s;
    set<int> main;
    for (int i=0; i<n; i++){
        cin >> d;
        int diff = s-d;
        auto it = find(main.begin(), main.end(), diff);
        if (it != main.end()){
            cout << d << " " << diff;
            ok = 0;
            break;
        }else{
            main.insert(d);
        }
    }
    cout <<(ok ? "-1\n" : "\n");

}