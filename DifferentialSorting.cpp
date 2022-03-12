#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int t;
    while (t--){
        int n, d, i;cin>>n;
        vector<int> A;
        for(i=0; i<n; i++){
            cin >>d;
            A.push_back(d);
        }
        if (A[n-1] < A[n-2]){
            cout << -1<<"\n";
            continue;
        }
        else if (A[n-1]<0){
            if (is_sorted(A.begin(), A.end())){
                cout << 0<<"\n";
            }
            else{cout << -1<<"\n";}
            continue;
        }
        cout << n-2;
        for (i=1; i<=n-2; i++){
            cout << i << " " << n-1 << " " << n<< "\n";
        }
    }
}
