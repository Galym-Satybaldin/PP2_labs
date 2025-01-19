#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main(){
    string sent;
    getline(cin, sent);
    stringstream ss (sent);
    string word;
    int count;
    while (ss>>word){
        count++;
    }
    cout<<count;

    return 0;
}