#include <bits/stdc++.h>
using namespace std;

int main(){

    int n = 0;
    cin>>n;

    int x = 0;
    cin>>x;

    vector <int> arr;

    for (int i = 0; i<n; ++i){
        int c = 0;
        cin>>c;
        arr.push_back(c);
    }

    int count = 0;

    for (int i = 0; i<n; ++i){
        if (arr[i]==x){
            count ++;
        }
    }

    cout<<count<<endl;
    return 0;
}