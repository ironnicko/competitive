#include <vector>
#include <queue>
#include <set>
#include <iostream>



using namespace std;

typedef long long ll;

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     int d, s, n; cin >> n;
//     bool ok=1;
//     cin >> s;
//     set<int> main;
//     for (int i=0; i<n; i++){
//         cin >> d;
//         int diff = s-d;
//         auto it = find(main.begin(), main.end(), diff);
//         if (it != main.end()){
//             cout << d << " " << diff;
//             ok = 0;
//             break;
//         }else{
//             main.insert(d);
//         }
//     }
//     cout <<(ok ? "-1\n" : "\n");

// }


// int main(){
//     int n;
//     cin>>n;
//     int sum1 =0,sum2=0;
//     int a[n][n]
//     for(int i=0;i<n;i++){
//         for(int j=0;j<n;j++){
//             cin>>a[i][j];
//         }
//     }
//     for(int i=0;i<n;i++){
//             sum1+=a[i][i];
//             sum2+=a[i][n-i-1];
//     }
//     cout << abs(sum2-sum1) << "\n";
//     return 0;
// }

// Bottom-Top approach
// void test(){
//     Node* head = new Node();

// }

// int fib(int n){
//     if(n==1 || n==2){
//         return 1;
//     }
//     vector<int> bottom_up(n+1);
//     bottom_up[1] = 1;
//     bottom_up[2] = 1;
//     for (int i=3; i<n+1; i++){
//         bottom_up[i] = bottom_up[i-1] + bottom_up[i-2];
//     }
//     return bottom_up[n];
// }

// // Memoised approach 
// int fib_juiced(int n, map<int, int> &memo){
//     int result;
//     if (n==1 || n==2){
//         return 1;
//     }
//     if (memo.find(n) != memo.end()){
//         return memo[n];
//     }
//     result = fib_juiced(n-1, memo) + fib_juiced(n-2, memo);
//     memo[n] = result;
//     return memo[n];
// }

// int main(){
//     map<int, int> memo;
//     int n;
//     cin >> n;
//     cout << fib_juiced(n, memo);
// } 
// int main(){
//     int t;
//     while (t--){
//         int no[1002],chef[1002],as[1002], n, m, i, temp;
//         scanf("%i %i", &n, &m);
//         for (i=1; i<n; i++){
//             chef[i] = i;
//         }
//         while (i=0; i<m; i++){
//             scanf("%d", &temp);
//             chef[temp] = -1;
//         }
//         for (i=1; i<)
//     }
// }

// int main(){
//     vector<vector<int>> adj; 
//     int n; 
//     int s; 

//     queue<int> q;
//     vector<bool> used(n);
//     vector<int> d(n), p(n);

//     q.push(s);
//     used[s] = true;
//     p[s] = -1;
//     while (!q.empty()) {
//         int v = q.front();
//         q.pop();
//         for (int u : adj[v]) {
//             if (!used[u]) {
//                 used[u] = true;
//                 q.push(u);
//                 d[u] = d[v] + 1;
//                 p[u] = v;
//             }
//         }
//     }
// }

// vector<ll> dp(100000, 0);

// ll fib(int n){
//     if (dp[n]) return dp[n];
//     if (n<3) return 1;
//     dp[n] = fib(n-1) + fib(n-2);
//     return dp[n];
// }

// int main(){
//     cout << fib(100);
// //    char str[20];
// //    scanf("%[^\n]%*c", str);
// //    printf("%s", str);
//     return 0;
// }

// int main(){
//     int N ; cin>> N;
//     int primes[N+1];
//     for (int i =0; i < N+1; i++) primes[i] = 0;
//     for (int i=2; i< N+1; i++){
//         for (int j = i*i; j< N; j+=i){
//             primes[j] = 1;
//         }
//     }
//     cout << primes[N];
// }
