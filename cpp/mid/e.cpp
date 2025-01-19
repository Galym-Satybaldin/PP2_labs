#include <iostream>
#include <c++.stdh>
using namespace std;

int add(int a, int b){
    return a + b;
}

int main() {
    int a; 
    int b;
    cin>>a>>b;
    cout<<add(a,b)<<endl;

    return 0;
}