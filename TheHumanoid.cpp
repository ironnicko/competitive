#include<iostream>

using namespace std;

typedef long long ll;

int recurr(ll n, ll arr[], int i, int g, int b, ll h){
    if (i >= n) return 0;
    if (h > arr[i]) return recurr(n, arr, i+1, g, b, h + (arr[i]/2))+1;
    else{
        int take_b = 0, take_g= 0;
        if (b) take_b = recurr(n, arr, i, g, b-1, h*3);
        if (g) take_g = recurr(n, arr, i, g-1, b, h*2);
        return max(take_b, take_g);
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    while (t--){
        ll n, h; cin >> n >> h;
        ll arr[n]; for (ll &i : arr) cin >> i;
        sort(arr, arr+n);
        cout << recurr(n, arr, 0, 2, 1, h)<<"\n";
    }
}