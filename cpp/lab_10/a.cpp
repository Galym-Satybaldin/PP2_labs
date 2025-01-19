#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    map<int, int> freq;

    // Input elements and count frequencies
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        freq[arr[i]]++;
    }

    // Find the most frequent element
    int mostFrequent = arr[0];
    int maxCount = 0;

    for (map<int, int>::iterator it = freq.begin(); it != freq.end(); ++it) {
        if (it->second > maxCount || (it->second == maxCount && it->first < mostFrequent)) {
            maxCount = it->second;
            mostFrequent = it->first;
        }
    }

    cout << mostFrequent << endl;

    return 0;
}
