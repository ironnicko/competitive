#include <bits/stdc++.h>
#include <time.h>

using namespace std;

typedef long long ll;

int main(void){
    clock_t tStart = clock();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while(t--){
        int n; cin >> n;
        vector<int> a(n);
        for (int &i : a){
            cin >> i;
        }
        string s; cin >> s;
        vector<int> r, b;
        for(int i=0; i<n; i++){
            if (s[i] == 'R'){
                r.push_back(a[i]);
            } else{
                b.push_back(a[i]);
            }
        }
        sort(b.begin(), b.end());
        sort(r.begin(), r.end());
        reverse(r.begin(), r.end());
        bool ok = 1;
        for (int i=0; i<r.size(); i++){
            if (r[i] > n-i){
                ok = 0;
            }
        }
        for (int i=0; i<b.size(); i++){
            if (b[i] < i+1){
                ok = 0;
            }
        }
        cout << (ok ? "YES" : "NO")<< "\n";

    }
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}