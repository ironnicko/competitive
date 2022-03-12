#include<bits/stdc++.h>
using namespace std;
 
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        vector<int>ans(n);
        for(int i = n-1;i>=0;i--)
        {
            ans[i] = a[i];
            int j = i+a[i];
            if(j<n)
            {
                ans[i]+=ans[j];
            }
        }
        cout<<*max_element(ans.begin(),ans.end())<<endl;
    }
}