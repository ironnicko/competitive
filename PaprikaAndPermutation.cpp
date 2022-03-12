#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;cin >> n;
        set<int> A_set;
        for (int i=1; i<=n; i++){A_set.insert(i);}
        vector<int> A;
        for (int i=0; i<n; i++){
            int v;cin >> v;
            if (A_set.find(v) != A_set.end()){A_set.erase(v);}
            else{A.push_back(v);}
        }
        sort(A.begin(), A.end());
        reverse(A.begin(), A.end());
        int p=0;bool flag=0;
        for (auto &nx : A){
            auto it=A_set.end();
            it--;
            int ctg=(*it);
            if (ctg>(nx-1)/2){flag=true; break;}
            A_set.erase(it);
        }
        if (flag){cout<<"-1\n";}
        else{cout << A.size() <<"\n";}
    }
}