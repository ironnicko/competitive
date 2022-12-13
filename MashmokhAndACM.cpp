#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define MOD 1000000007

int recurr(int n, int k, int i, vector<vector<int> > &dp)
{
    if (k <= 0)
        return 1;
    if (dp[i][k] != -1)
        return dp[i][k];
    int ans = 0;
    for (int j = i; j <= n; j += i)
    {
        ans += recurr(n, k - 1, j, dp) % MOD;
        ans %= MOD;
    }
    dp[i][k] = ans;
    return dp[i][k];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    vector<vector<int> > dp(n + 1, vector<int>(k + 1, -1));

    cout << recurr(n, k, 1, dp);
}