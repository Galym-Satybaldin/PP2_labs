#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>  // for sorting

using namespace std;

int main() {
    int n = 0;
    cin >> n;
    cin.ignore(); // Ignore the leftover newline after reading `n`

    vector<string> words;
    vector<string> uniqueValidWords;

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        string word;

        while (ss >> word) {
            words.push_back(word);
        }
    }

    for (int i = 0; i < words.size(); i++) {
        string word = words[i];
        int countLower = 0, countUpper = 0, countDigit = 0;
        
        // Count lowercase, uppercase, and digits in the word
        for (int j = 0; j < word.size(); j++) {
            if (word[j] >= 'a' && word[j] <= 'z') {
                countLower++;
            } else if (word[j] >= 'A' && word[j] <= 'Z') {
                countUpper++;
            } else if (word[j] >= '0' && word[j] <= '9') {
                countDigit++;
            }
        }

        // If the word has at least one of each type, check for uniqueness and add it
        if (countLower > 0 && countUpper > 0 && countDigit > 0) {
            bool isUnique = true;
            for (int k = 0; k < uniqueValidWords.size(); k++) {
                if (uniqueValidWords[k] == word) {
                    isUnique = false;
                    break;
                }
            }

            if (isUnique) {
                uniqueValidWords.push_back(word);
            }
        }
    }

    // Sort the unique valid words in lexicographical order
    sort(uniqueValidWords.begin(), uniqueValidWords.end());

    // Print the count and the unique valid words
    cout << uniqueValidWords.size() << endl;
    for (int i = 0; i < uniqueValidWords.size(); i++) {
        cout << uniqueValidWords[i] << endl;
    }

    return 0;
}
