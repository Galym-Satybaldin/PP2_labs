#include <iostream>
#include <cmath>
#include <string>

using namespace std;

char changeRegister (char n){
    if (n>='a' && n<='z'){
        n = n - 32;
        return n;
    }

    else if (n>='A' && n<='Z'){
        n = n + 32;
        return n;
    }

    else {
        cout<<"error";
    }

}

int main(){
    char n;
    cin>>n;
    cout<<changeRegister(n);
    return 0;
}