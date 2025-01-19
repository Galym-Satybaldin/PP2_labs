#include <bits/stdc++.h>
using namespace std;

int main(){
    int n = 0; 
    cin>>n;
    int arr[n] = {};

    for (int i = 0; i<n; ++i){
        cin>>arr[i];
    }

    set <int> arr1;

    for (int i = 0; i<n; ++i){
        arr1.insert(arr[i]);
    }

    int count = 0;

    for (int i = 0; i<arr1.size(); ++i){
        count ++;
    }

    cout<<count<<endl;

    return 0;
}