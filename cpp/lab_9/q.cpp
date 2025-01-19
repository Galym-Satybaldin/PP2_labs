#include <iostream>
#include <algorithm>
#include <vector>

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

    vector<int>::iterator it = unique(vec.begin(), vec.end());

    vec.erase(it, vec.end());

    for (int i = 0; i<vec.size(); ++i){
        cout<<vec[i]<<" ";
    }


    return 0;
}