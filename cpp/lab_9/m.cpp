#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    
    int n = 0;
    cin>>n;
    int size = (n*(n+1))/2;

    vector <int> vec(size);

    int start = 0;
    for (int i = 1; i<=n; ++i){
        fill(vec.begin()+start,vec.begin()+start+i, i);
        start += i;
    }

    for (int i = 0; i<vec.size(); ++i){
        cout<<vec[i]<<" ";
    }
    

    return 0;

}