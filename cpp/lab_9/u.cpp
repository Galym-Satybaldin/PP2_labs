#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> arr(n);
    vector<int> sortedArr(n);

    for (int j = 0; j < n; ++j) {
        cin >> arr[j];
        sortedArr[j] = arr[j];  // Copy arr to sortedArr for sorting
    }

    sort(sortedArr.begin(), sortedArr.end());  // Sort the copy for comparison

    vector<int> mismatches;

    for (int i = 0; i < n; ++i) {
        if (arr[i] != sortedArr[i]) {
            mismatches.push_back(i);  // Record indices of mismatched elements
        }
    }

    if (mismatches.size() == 2) {
        // Swap the mismatched elements
        swap(arr[mismatches[0]], arr[mismatches[1]]);
        if (arr == sortedArr) {
            cout << "YES";
        } else {
            cout << "NO";
        }
    } else if (mismatches.size() == 0) {
        // Already sorted
        cout << "YES";
    } else {
        // More than two mismatches or unhandled case
        cout << "NO";
    }

    return 0;
}
