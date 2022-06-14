#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	while(t--){
		int n, y=0,temp=10000001, idx=0;cin >> n;
		vector<int> a(n);
		if (n != 0){
			for (int &i : a){
				cin >> i;
				y = (i < temp ? idx : y);
				idx += 1;
				temp = a[idx-1];
			}
			cout << (y ? n : n-1)<< "\n";
			for (int i=0; i < n; i++){
				if (i==y){
					continue;
				}
				cout << i + 1 <<" " << y + 1 <<" " << a[y] + i <<" " << a[y]<<"\n";
			}
			if (y) cout << 1 <<" " << y + 1 <<" " << a[y] <<" " << a[y] + y<<"\n";
		} else {
			cout << 0 << "\n";
		}
	}
}