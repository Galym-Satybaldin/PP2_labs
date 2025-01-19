#include <iostream>
#include <string>

using namespace std;

int main(){

    int n = 0;
    cin>>n;

    string arr[n][n];

    for (int i = n-1; i>=0; --i){
        for (int j = 0; j<n; ++j){
            arr[i][j] = '*';
        }    
    }

    for (int i = 0; i<n; ++i){
        for (int j = 0; j<n; ++j){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
}