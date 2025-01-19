#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool match(string s1, string s2){

    s1.erase(remove(s1.begin(), s1.end(), ' '), s1.end());
    s2.erase(remove(s2.begin(), s2.end(), ' '), s2.end());

    if (s1 == s2){
        return true;
    }
    else {
        return false;
    }
}

int main(){
    string s1;
    string s2;
    getline (cin, s1); 
    getline (cin, s2);

    

    if (match(s1,s2) == true){
        cout<<"yes";
    }
    else {
        cout<<"no";
    }




    return 0;
}