#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int n = 0;
    cin>>n;
    string array1[n];
    for (int i = 0; i<n; ++i){
        cin>>array1[i];
    }

    int m = 0;
    cin>>m;
    
    vector <string> array2;

    for (int i = 0; i<m; ++i){
        string line;
        getline (cin, line);
        string x;

        stringstream ss(line);
        while (ss>>x){
            array2.push_back(x);
        }
    }



    for (int i = 0; i<n; ++i){
        for (int j = 0; j<m; ++j){
            if (i!=n && j!=m && array1[i]==array2[j] && array1[i+1]==array2[j+1]){
                cout<<array1[i]<<" "<<array2[i+1]<<endl;
            }
        }
    }





    return 0;
}