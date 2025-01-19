#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n, m; 
    cin>>n>>m;

    vector <int> arr1;
    vector <int> arr2;

    for (int i = 0; i<n; ++i){
        int x;
        cin>>x;
        arr1.push_back(x);
    }
    for (int i = 0; i<m; ++i){
        int x;
        cin>>x;
        arr2.push_back(x);
    }

    vector <int>:: iterator it = unique(arr1.begin(), arr1.end());
    arr1.erase(it, arr1.end());

    vector <int>:: iterator it1 = unique(arr2.begin(), arr2.end());
    arr2.erase(it1, arr2.end());

    vector <int> merged;

    int i = 0, j = 0;
    while (i<arr1.size() || j<arr2.size()){
        if (i<arr1.size()){
            merged.push_back(arr1[i]);
            ++i;
        }
        if (j<arr2.size()){
            merged.push_back(arr2[j]);
            ++j;
        }
    }

    vector <int>:: iterator iter = unique(merged.begin(), merged.end());
    merged.erase(iter, merged.end());


    for (int i = 0; i<merged.size(); ++i){
        cout<<merged[i]<<" ";
    }

    return 0;
}