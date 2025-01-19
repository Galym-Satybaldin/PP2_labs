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
    cin.ignore();

    for (int i = 0; i<n; ++i){
        string line;
        getline (cin, line);
        string x;
        stringstream ss (line);
        vector <string> all;
        while (ss>x){
            names.push_back(x);
        }
    }

    vector <string> names;
    for (int i = 0; i<all.size(); i=i+2){
        names.push_back(all[i]);
    }

    sort (names.begin(), names.end());


    vector <string> attended;
    for (int h = 0; h<names.size(); ++h){
        int count = 0;
        string sample = names[h];
        for (int i = 0; i<names.size(); ++i){
            if (sample == names[i]){
                count ++;
            }
            if (count >= 3){
                attended.push_back(sample);
            }
        }
    }

    set <string> s;
    for (int i = 0; i<names.size(); ++i){
        s.insert(names[i]);
    }

    for (int i = 0; i<attended.size(); ++i){
        for (char c : s) {
            if (attended[i] == )
        }
    }

    for (int i = 0; i<attended.size(); ++i){
        cout<<attended[i]<<"+1"<<endl;
    }



}