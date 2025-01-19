#include <bits/stdc++.h>
using namespace std;

int main(){
    int n = 0; 
    cin>>n;
    
    map <string, int> numbers;

    for (int i = 0; i<n; ++i){
        string x; 
        cin>>x;
        numbers[x]++;
    }

    int countThree = 0;

    for (map<string,int>:: iterator it = numbers.begin(); it!=numbers.end(); ++it){
        if (it->second==3){
            countThree++;
        }
    }

    cout<<countThree<<endl;

    return 0;
}