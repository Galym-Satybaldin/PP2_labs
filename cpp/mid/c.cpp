#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    int n = 0;
    cin>>n;
    int arr[n] = {};
    for (int i = 0; i<n; ++i){
        cin>>arr[i];
    }
    int newarr[n] = {};
    int counteven = 0;

    for (int i = 0; i<n; ++i){
        if (arr[i]%2==0){
            newarr[counteven] = arr[i];
            counteven ++;
        }
    }
//find the number of even elements in array
//find last even element in array
    for (int i = 0; i<n; ++i){
        if (arr[i]%2!=0){
            newarr[counteven] = arr[i];
            counteven++;
        }
    }
    // Output the rearranged array
    for (int i = 0; i < n; ++i) {
        cout << newarr[i] << " "; // Print each element
    }
    cout << endl; // New line at the end

    return 0;
}
