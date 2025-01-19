#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n = 0;
    cin>>n;

    string arr[n];
    for (int i = 0; i<n; ++i){
        cin>>arr[i];
    }

    for (int i = 0; i<n; ++i){
        sort(arr[i].begin(), arr[i].end());
    }

    for (int i = 0; i<n; ++i){
        cout<<arr[i]<<endl;
    }

    for (int i = 1; i<n; ++i){
        for (int j = 0; j<arr[i].size(); ++j){
            
        }
    }

    return 0;
}