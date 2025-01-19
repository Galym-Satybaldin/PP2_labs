#include <bits/stdc++.h>
using namespace std;

int main(){

    string word;
    cin>>word;

    int counter = 0;

    for (int i = 0; i<word.size(); ++i){
        char c = word[i];
        if (c=='('){
            counter++;
        }
        else if (c==')'){
            counter--;
        }

        if (counter<0){
            cout<<"NO"<<endl;
            return 0;
        }
    }

    if (counter == 0){
        cout<<"YES"<<endl;
    }
    else {
        cout<<"NO"<<endl;
    }
    return 0;
}