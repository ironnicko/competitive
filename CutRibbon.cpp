#include <bits/stdc++.h>

using namespace std;

int dp[4001];
int n, a, b, c;

int x(int r)
{
	if(r<0) return -1;
	if(r==0) return dp[r]=0;
	if(dp[r]!=0) return dp[r];

	return dp[r]=1+max(x(r-a),max(x(r-b), x(r-c))); // we're getting the maximum of the three differences between the 3 no.s
}

int main()
{
	cin>>n>>a>>b>>c;
	cout<<x(n);
}
  	 		   				 		 	  			 	  		 	