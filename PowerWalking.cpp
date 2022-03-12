#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    
    cin >> t;
    while (t--){
        int n, d, i;
        cin >> n;
        set<int> arrayset;
        for (i=0; i<n; i++){
            cin >> d;
            arrayset.insert(d);
        }
        int length = arrayset.size();
        int some = n - length;
        for (i=n; i>some; i--){
            cout << length << " ";
        }
        length += 1;
        for (i=0; i<some; i++){
            cout<< length + i<< " ";
        }
        cout << "\n";

    }
}
