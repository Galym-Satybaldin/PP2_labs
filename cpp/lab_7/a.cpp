#include <bits/stdc++.h>
#include <set>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int main (){

    string line;
    getline (cin, line);
    stringstream ss (line);
    int x;

    int n = 0, r = 0;
    ss>>n>>r;

    for (int i = 0; i<n; ++i){
        for (int j = 0; j<n; ++j){
            arr[i][j] = 0;
        }
    }

    vector <int> coordinates;
    for (int i = 0; i<r; ++i){
        string point;
        getline (cin, point);
        stringstream ss (point);
        int h;
        while (ss>>h){
            coordinates.push_back(h);
        }
    }

    for (int u = 0; u<r; ++u){
        int count;
        if (count != 0){
        //filling rows (odd elements of coordinates with ones)
            for (int k = 0; k<n; k = k+2){
                for (int j = 0; j<n; ++j){
                    arr[coordinates[k]][j] = 1;
                }
            }

        //filling colomns (evens) with ones
            for (int i = 0; i<n; ++i){
                for (int k = 1; k<n; k = k+2){
                    arr[i][coordinates[k]] = 1;
                }
            }
            
            count = -1;

            for (int i = 0; i<n; ++i){
                for (int j = 0; j<n; ++j){
                    if (arr[i][j] = 0){
                        count++;
                    }
                }
            }
                
            cout<<count;
            }
            else if (count == 0){
                cout<<0;
                return 0;
            }
    }

    return 0;
}