#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main(){
    string sent;
    getline(cin, sent);
    stringstream ss (sent);
    string word;
    vector <string> arr;

    while (ss>>word){
        arr.push_back(word);
    }
    string biggest = "";

    for (int i = 1; i<arr.size(); ++i){
        if (arr[i].size() > biggest.size()){
            biggest = arr[i];
        }
    }

    cout<<biggest.size();

    return 0;
}