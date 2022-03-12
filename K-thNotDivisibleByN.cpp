#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n, k;
        cin >> n >> k;
        ll result = (k/(n-1)) * n;
        if (n > k){
            result = k;
        }
        else{
            int rem = k % (n-1);
            if (!rem){
                rem = -1;
            }
            result += rem;
        }
        cout << result << "\n";
    }
}