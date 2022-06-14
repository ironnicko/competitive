#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    string s; cin >> s;
    int maxi = 0, current=0;
    for (int i=1; i<s.length(); i++){
        if (s[i-1] == s[i]){
            current += 1;
        }
        else{
            maxi = max(current, maxi);
            current = 0;
        }
    }
    maxi = max(current, maxi);
    cout << maxi+1;
    
}