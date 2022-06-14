#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;cin >> n;   
    int a[n];
    int even=0, odd=0;
    int even_num, odd_num;
    int temp;
    for (int i=0; i<n; i++){
        cin >> temp;
        a[i] = temp;
        if (temp%2){
            odd++;
            odd_num = i+1;
        } else{
            even++;
            even_num = i+1;
        }
    }
    cout << (odd == 1 ? odd_num : even_num);
}