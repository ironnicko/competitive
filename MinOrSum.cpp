#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n, d, t, last=0;
    cin>>t;
    while (t--){
        cin >> n;
        vector<int> array;
        for (int i = 0; i<n; i++ ){
            cin >> d;
            last |= d;
        }
        cout<<last<<endl;
        last = 0;
    }
}