#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int number;
        cin >> number;
        number %= (int)1e5 + 16;
        string str;
        cin >> str;
        ll final = 0;
        for (int i = 0; i < number; i++)
        {
            vector<int> zeronine(10);
            int not_there = 0;
            for (int j = i; j < min(i + 228, number); j++)
            {
                auto c = str[j] - '0';
                not_there+=zeronine[c] == 0;
                zeronine[c]++;
                final+=(*max_element(zeronine.begin(), zeronine.end()) <= not_there);
            }
        }
        cout << final << endl;
    }
}