#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    int n, k;
    cin >> n >> k;
    bool flag = 1;
    if (k > n-1){
        cout << -1 << "\n";
    }
    else{
        int current=0, last = n-1, operations = n - k -1;
        vector<int> numbers;
        for (int i=1; i<=n; i++){
            numbers.push_back(i);
        }
        while (operations > 0){
            operations -= 1;
            swap(numbers[current], numbers[last]);
            last -= 1;
        }
        for (int j : numbers){
            cout << j << " ";
        }
    }
}