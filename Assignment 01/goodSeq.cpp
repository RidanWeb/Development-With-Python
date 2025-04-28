#include <bits/stdc++.h>
using namespace std;




int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    
    vector<int> a(n);
    unordered_map<int, int> freq;

    for(int i = 0; i < n; i++){

        cin >> a[i];
        freq[a[i]]++;
    }

    
    int count = 0;

    for(auto [num, f] : freq){

        if(f < num){
            
            count += f;
            
        }else if(f > num){
            
            count = count + (f - num);
        }
    }
    
    cout << count;






    return 0;
}