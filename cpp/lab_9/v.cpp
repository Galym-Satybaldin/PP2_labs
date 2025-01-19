#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    string word;
    cin>>word;

    vector <string> words;
    cout<<"The anagram variants for string " <<word<< " are:"<<endl;
    sort (word.begin(), word.end());
    do{
        words.push_back(word);
    }while (next_permutation(word.begin(), word.end()));

    for (int i = 0; i<words.size(); ++i){
            cout<<words[i]<<endl;
    }
    return 0 ;
}

