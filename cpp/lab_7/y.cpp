#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n; // Number of assistants
    cin >> n;

    // Map to store student-to-assistant relationships
    map<string, string> studentMap;
    string mentor;
    int studentCount;
    string student;

    // Read each assistant and their students
    for (int i = 0; i < n; ++i) {
        cin >> mentor; // Read assistant's name
        cin >> studentCount; // Read number of students

        // Read the names of the students
        for (int j = 0; j < studentCount; ++j) {
            cin >> student;
            // Map the student to the assistant (last one overrides)
            studentMap[student] = mentor;
        }
    }

    int h; // Number of requests
    cin >> h;
    cin.ignore(); // Ignore newline character after reading 'h'

    // Process each request and print the result
    for (int i = 0; i < h; ++i) {
        string query;
        getline(cin, query);

        // Check if the student exists in the map and print the result
        if (studentMap.find(query) != studentMap.end()) {
            cout << studentMap[query] << endl;
        } else {
            cout << "F" << endl; // Student not found
        }
    }

    return 0;
}
