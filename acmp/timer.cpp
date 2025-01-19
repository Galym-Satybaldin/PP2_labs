#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>

using namespace std;

int main(){
    string line;
    getline(cin, line);

    int x;
    stringstream ss (line);
    vector <int> initialTime;
    while (ss>>x){
        if (x==':'){
            continue;
        }
        else {
            initialTime.push_back(x);
        }
    }



    string line1;
    getline(cin, line1);

    int x1;
    stringstream ss (line1);
    vector <int> initialTime1;
    while (ss>>x1){
        if (x1==':'){
            continue;
        }
        else {
            initialTime.push_back(x1);
        }
    }








    return 0;
}