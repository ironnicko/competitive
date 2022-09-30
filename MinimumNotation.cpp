
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;cin >> t;
    while(t--){
        string s;cin>>s;
        reverse(s.begin(), s.end());
        int n = s.size(), chr = (int)'9';
        n %= 1000000;
        vector<int> track(10, 0);
        for (char iter : s){
            if (iter <= char(chr)){
                track[iter - '0']+=1;
                chr = iter;
            }
            else{
                if(iter != '9'){
                    track[iter - '0' + 1]++;
                }
                else{
                    track[9]++;
                }
            }
        }
        for (int i = 0;i<10;i++){
            while(track[i]--){
                cout << i;
            }
        }
        cout << endl;
    }
}