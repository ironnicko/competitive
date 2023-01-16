#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        int n, initial_power;
        cin >> n >> initial_power;
        int final_ans = initial_power;
        vector<int> health_monster(n), power_monster(n);
        for (int i = 0; i < n; i++)cin >> health_monster[i];for (int i = 0; i < n; i++)cin >> power_monster[i];
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> qu;
        for (int i = 0; i < n; i++){
            qu.push({power_monster[i], health_monster[i]});
        }

        while (initial_power>0 && !qu.empty())
        {
            while ((!qu.empty()) && (qu.top().second <= final_ans)){
                qu.pop();
            }
            initial_power -= qu.top().first;
            final_ans += initial_power;
        }
        if (!qu.empty()) cout << "NO";
        else{
             cout << "YES";
        }
        cout << endl;
    }
}