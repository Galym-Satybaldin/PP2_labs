#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>

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

    set <int> numbers;

    for (int i = 0; i<n; ++i){
        numbers.insert(arr[i]);
    }

    set <int> :: iterator it;

    vector <int> uniqueNumbers;

    for (it = numbers.begin(); it!= numbers.end(); ++it){
        uniqueNumbers.push_back(*it);
    }

    sort(uniqueNumbers.begin(), uniqueNumbers.end());

    do{
        for (int i = 0; i<uniqueNumbers.size(); ++i){
            if(i> 0) {cout<<" ";}
            cout<<uniqueNumbers[i];
        }
        cout<<endl;
    }while(next_permutation(uniqueNumbers.begin(), uniqueNumbers.end()));


    return 0;
}