#include <bits/stdc++.h>
using namespace std;

#define ll long long 


int main()
{

    int t; cin >> t;
    while(t--)
    {
        ll n; cin >> n;
        if(n == 1) 
        {
            cout << "NO" << "\n";
            continue;
        }

        ll x = sqrt(n);
        if(x * x == n)
        {
            ll cnt = 0;
            for(ll i = 1; i <= sqrt(x); i++)
            {
                if(x % i == 0) cnt++;
            }

            if(cnt == 1) cout << "YES" << "\n";
            else cout << "NO" << "\n";
        }

        else
        cout << "NO" << "\n";

    }
}
