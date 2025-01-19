#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n = 0;
    cin>>n;

    vector <int> arr;

    for (int i = 0; i<n; ++i){
        int x;
        cin>>x;
        arr.push_back(x);
    }

    vector <int> arr2;
    arr2 = arr;
    reverse(arr2.begin(), arr2.end());


    for (int i = 0; i<n; ++i){
        if (arr[i] == arr2[i]){
            cout<<"OK"<<endl;
        }
        else {
            cout<<"Instead of "<<arr[i]<<" here was "<<arr2[i]<<endl;
        }
    }


    return 0;
}