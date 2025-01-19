#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n;
    cin.ignore(); // Ignore newline after reading n

    set<string> firstAccount;
    set<string> secondAccount;

    // Read the first account subscriptions
    for (int i = 0; i < n; ++i) {
        string account;
        getline(cin, account);
        firstAccount.insert(account);
    }

    cin >> m;
    cin.ignore(); // Ignore newline after reading m

    // Read the second account subscriptions
    for (int i = 0; i < m; ++i) {
        string account;
        getline(cin, account);
        secondAccount.insert(account);
    }

    // Convert sets to vectors for index-based iteration
    vector<string> firstAccountVec(firstAccount.begin(), firstAccount.end());
    vector<string> secondAccountVec(secondAccount.begin(), secondAccount.end());

    // Find unique names in either account but not both
    vector<string> result;

    // Loop through firstAccountVec and check if names are not in secondAccount
    for (int i = 0; i < firstAccountVec.size(); ++i) {
        if (secondAccount.find(firstAccountVec[i]) == secondAccount.end()) {
            result.push_back(firstAccountVec[i]);
        }
    }

    // Loop through secondAccountVec and check if names are not in firstAccount
    for (int i = 0; i < secondAccountVec.size(); ++i) {
        if (firstAccount.find(secondAccountVec[i]) == firstAccount.end()) {
            result.push_back(secondAccountVec[i]);
        }
    }

    // Sort the result to print in ascending order
    sort(result.begin(), result.end());

    // Print the sorted unique names
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << endl;
    }

    return 0;
}