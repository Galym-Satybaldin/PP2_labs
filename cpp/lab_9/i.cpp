#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int main(){
    int n = 0;
    cin>>n;

    vector <int> vec;

    for (int i = 0; i<n; ++i){
        int x;
        cin>>x;
        vec.push_back(x);
    }

    sort(vec.begin(), vec.end());

    vector <int>::iterator it = unique(vec.begin(), vec.end());
    vec.erase(it, vec.end());


    do{
        for (int i = 0; i<vec.size(); ++i){
            cout<<vec[i]<<" ";
        }
        cout<<endl;
    }
    while(next_permutation(vec.begin(), vec.end()));
    



    return 0;
}