#include <string>
#include <iostream>

using namespace std;

int main(){
    int t;
    cin >>t;
    string main="rgb";
    while (t--){
        string item;
        cin >> item;
        bool flag = true;
        for (char j : main){
            char upper = toupper(j);
            if (item.find(j) > item.find(upper)){
                flag = false;
                break;
            }
        }
        if (flag){
            cout << "YES"<<endl;
        }
        else{
            cout << "NO"<<endl;
        }
        
    }
}