#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        vector<int> main;

        for (int i=0; i<n; i++){
            int d;
            cin >> d;
            main.push_back(d);
        }
        if (n == 1){
            cout << "YES\n";
            continue;
        }

        sort(main.begin(), main.end());

        for (int j=1 ; j<n; j++){
            if (main[j] - main[j-1] <= 1){
                n -= 1;
            }
        }
        if (n==1){
            cout << "YES";
        }
        else{
            cout << "NO";
        }
        cout << "\n";
    }
}