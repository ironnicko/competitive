#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N=1e5+3,mod=1e9+7;
int n,a[N],p[N],l,r;
ll solve(){
	cin>>n;
	for(int i=0;i<n;++i)cin>>a[i],p[a[i]]=i;
	int l=p[0],r=p[0];
	ll res=1;
	for(int i=1;i<n;++i){
		if(p[i]>l&&p[i]<r)(res*=r-l-i+1)%=mod;
		else if(p[i]<l)l=p[i];
		else if(p[i]>r)r=p[i];
	}
	return res;
}

int main(){
	ios::sync_with_stdio(0);cin.tie(0);
	int T;
	cin>>T;
	while(T--)cout<<solve()<<'\n';
}