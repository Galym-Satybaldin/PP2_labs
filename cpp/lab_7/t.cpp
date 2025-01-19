#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <map>

using namespace std;

int main() {
    string line;
    getline (cin, line);
    string x;

    vector <string> numbers;

    stringstream ss(line);

    while (ss>>x){
        numbers.push_back(x);
    }

    string a = numbers[0];
    string b = numbers[1];
        

    

    bool isUnique = false;

    for (int i = 0; i<a.size(); ++i){
        for (int z = 0; z<a.size(); ++z){

            string pointer = a[z];
            if (i == z){
                continue;
            }
            else if (pointer != a[i]){
                isUnique = true;
            }
        }
    }

    if (a==b && isUnique){
        cout<<a<<endl;
    }



    



    return 0;
}