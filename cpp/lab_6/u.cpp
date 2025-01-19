#include <iostream>
#include <cmath>

using namespace std;

void maxnod(int n){
    cin>>n;
    int arr[n] = {};

    for (int i = 0; i<n; ++i){
        cin>>arr[i];
    }
    int arrnods[n] = {};

    for (int i = 0; i<n-1; ++i){
        for (int j = 0; j<arr[i]; ++j){
            
        }
    }

    int max = arrnods[0];
    for (int i = 0; i<n; ++i){
        if (arrnods[i]>max){
            max = arrnods[i];
        }
    }

}

int main(){

    int n = 0;
    maxnod(n);

    return 0;
}