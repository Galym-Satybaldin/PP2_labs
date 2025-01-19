#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    string line;
    cin >> line;

    sort(line.begin(), line.end());

    string line2 = line;
    string::iterator it = unique(line2.begin(), line2.end());
    line2.erase(it, line2.end()); 

    if (line.length() % line2.length() == 0 || line.length() % line2.length() == 1) {
        cout << "ZA WARUDO TOKI WO TOMARE";
    } else {
        cout << "JOJO";
    }

    return 0;
}
