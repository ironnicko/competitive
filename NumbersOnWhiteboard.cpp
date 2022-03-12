#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n,t;
    cin >> t;
    while (t--){
        cin >> n;
        cout << 2 <<endl;
        cout << n<<" "<< n-1<<endl;
        for (int i = n-2; i>0; i-- ){
            cout << i+2 <<" "<< i<<endl;
        }
    }
}