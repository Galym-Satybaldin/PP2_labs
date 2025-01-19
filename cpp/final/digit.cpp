#include <iostream>
#include <cmath>

using namespace std;

bool isDigit(char n){
    if (n >= '0' && n<= '9'){
        return true;
    }
    else {
        return false;
    }

}

int main(){
    char n;
    cin>>n;
    if (isDigit(n)){
        cout<<"yes";
    }
    else{
        cout<<"no";
    }

    return 0;
}