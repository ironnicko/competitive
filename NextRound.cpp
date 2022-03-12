#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,k,s;
    vector<int> scores;
    cin >> n >> k;
    for (int i=0; i<n; i++){
        cin>>s;
        scores.push_back(s);
    }
    int count = 0;
    for (int score : scores){
        if (score >= scores[k-1] && score > 0){
            count++;
        }
    }
    cout<<count; 

}