#include <iostream>
#include <vector>
using namespace std;

double determinant(vector<vector<double> > matrix, int n) { // Add space between >
    double det = 1;
    for (int i = 0; i < n; ++i) {
        if (matrix[i][i] == 0) {
            for (int j = i + 1; j < n; ++j) {
                if (matrix[j][i] != 0) {
                    swap(matrix[i], matrix[j]);
                    det *= -1;
                    break;
                }
            }
        }
        if (matrix[i][i] == 0)
            return 0;

        det *= matrix[i][i];
        for (int j = i + 1; j < n; ++j) {
            double factor = matrix[j][i] / matrix[i][i];
            for (int k = i; k < n; ++k) {
                matrix[j][k] -= factor * matrix[i][k];
            }
        }
    }
    return det;
}

int main() {
    int n;
    cin >> n;
    vector<vector<double> > matrix(n, vector<double>(n)); // Add space between >
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> matrix[i][j];
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            cout << matrix[i][j] << " ";
        cout << endl;
    }

    cout << "Determinant: " << determinant(matrix, n) << endl;
    return 0;
}
