#include <bits/stdc++.h>

using namespace std;

int main(){
    int middle1, t, n;
    cin >> t;
    while (t--){
        int i;
        vector<int> main;

        cin >> n;
        for (int i=1; i<=n; i++){
            main.push_back(i);
        }

        reverse( main.begin(), main.end() );
        for (int i=0; i<n; i++){
            cout << main[i]<<" ";
        }
        cout << "\n";
        for (i=n-1; i>0; i--){
            swap(main[i], main[i-1]);
            for (auto item : main){
                cout << item<<" ";
            }
            cout << "\n";
        }

    }
}