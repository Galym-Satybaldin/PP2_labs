#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int n = 0;
    cin>>n;
    vector <int> arr1;
    for (int i = 0; i<n; ++i){
        int x;
        cin>>x;
        arr1.push_back(x);
    }

    int m = 0;
    cin>>m;
    vector <int> arr2;
    for (int i = 0; i<m; ++i){
        int x;
        cin>>x;
        arr2.push_back(x);
    }

    vector <int> arr3;
    for (int i = 0; i<n; ++i){
        arr3.push_back(arr1[i]);
    }
    for (int i = 0; i<m; ++i){
        arr3.push_back(arr2[i]);
    }

    sort (arr3.begin(), arr3.end());

    for (int i = 0; i<n+m; ++i){
        cout<<arr3[i]<<" ";
    }


    return 0;
}