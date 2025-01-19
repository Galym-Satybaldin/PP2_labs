#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main() {

    map <string, pair <int, int> > gpa;

    int n = 0;
    cin>>n;

    string name;
    int value;

    for (int i = 0; i<n; ++i){
        cin>>name>>value;

        gpa[name].first += value;
        gpa[name].second += 1;

    }

    for (map<string, pair<int, int> > :: iterator it = gpa.begin(); it!= gpa.end(); ++it){
        string name = it-> first;
        int totalSum = it -> second.first;
        int count = it -> second.second;
        double average = static_cast<double>(totalSum) /count;

        cout<<name<<": "<<fixed<<setprecision(3)<<average<<endl;
    }




    return 0;
}
