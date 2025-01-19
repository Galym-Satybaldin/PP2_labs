#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string bin(string b){
    
}

int main(){
    int n = 0;
    cin>>n;

    vector <int> vec;
    vector <string> vec2;


    for (int i = 0; i<n; ++i){
        int x;
        cin>>x;
        vec.push_back(x);
    }

    for (int i = 0; i<n; ++i){
        int a = vec[i];
        string b;
        while (a>0){
            b += a%2 + '0';
            a /= 2;
        }
        if (b.empty()){
            b = "0";
        }
        reverse(b.begin(), b.end());
        vec2.push_back(b);
    }
    
    for (int i = 0; i<vec2.size(); ++i){
        cout<<vec2[i]<<endl;;
    }
    
    return 0;

}