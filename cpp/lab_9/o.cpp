#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> vec(n);

    for (int i = 0; i < n; ++i) {
        cin >> vec[i];
    }

    sort(vec.begin(), vec.end());

    // Count odd frequencies and check palindrome possibility
    vector<int> firstHalf, odd;
    for (int i = 0; i < n; ) {
        int count = 0, current = vec[i];
        while (i < n && vec[i] == current) {
            count++;
            i++;
        }
        // If the count is odd, add one occurrence to odd
        if (count % 2 != 0) {
            odd.push_back(current);
        }
        // Add half the occurrences to firstHalf
        for (int j = 0; j < count / 2; ++j) {
            firstHalf.push_back(current);
        }
    }

    // Check if more than one odd element exists
    if (odd.size() > 1) {
        cout << "Impossible" << endl;
        return 0;
    }

    // Construct the palindrome
    vector<int> palindrome = firstHalf;
    if (!odd.empty()) {
        palindrome.push_back(odd[0]); // Add the middle element
    }
    for (int i = firstHalf.size() - 1; i >= 0; --i) {
        palindrome.push_back(firstHalf[i]); // Add the reverse of firstHalf
    }

    // Output the result
    for (int i = 0; i< palindrome.size(); ++i) {
        cout << palindrome[i] << " ";
    }
    cout << endl;

    return 0;
}
