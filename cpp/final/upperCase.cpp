#include <iostream>
#include <cmath>
#include <string>

using namespace std;

char upperCase (char n){
    if (n>='a' && n<='z'){
        n = n - 32;
        return n;
    }

    else {
        return n;
    }

}

int main(){
    char n;
    cin>>n;
    cout<<upperCase(n);
    return 0;
}