#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n = 0;
    cin>>n;
    string line;
    getline (cin, line);
    string word;
    stringstream ss (line);
    vector <string> words;
    while (ss>>word){
        words.push_back(word);
    }

    set <string> characters;
    for (int i = 0; i<words[0].size(); ++i){
        characters.insert(words[0][i]);
    }

    set <string> rest;
    for (int i = 1; i<words.size(); ++i){
        for (int j = 0; j<words[i].size(); ++j){
            rest.insert(words[i][j]);
        }
    }

    set <string> common;
    for (int i = 0; i<characters.size(); ++i){
        for (int j = 0; i<rest.size(); ++j){
            if (characters[i]==rest[j]){
                common.insert(characters[i]);
            }
        }
    }

    for (int i = 0; i<common.size(); ++i){
        cout<<common[i]<<" ";
    }
    



    
    return 0;
}
