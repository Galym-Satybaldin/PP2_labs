#include <iostream>
#include <vector>
using namespace std;

bool getInverse(vector<vector<double> > &matrix, vector<vector<double> > &inverse, int n) {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            inverse[i][j] = (i == j) ? 1.0 : 0.0;

    for (int i = 0; i < n; ++i) {
        if (matrix[i][i] == 0) {
            for (int j = i + 1; j < n; ++j) {
                if (matrix[j][i] != 0) {
                    swap(matrix[i], matrix[j]);
                    swap(inverse[i], inverse[j]);
                    break;
                }
            }
        }
        if (matrix[i][i] == 0)
            return false;

        double diag = matrix[i][i];
        for (int j = 0; j < n; ++j) {
            matrix[i][j] /= diag;
            inverse[i][j] /= diag;
        }

        for (int k = 0; k < n; ++k) {
            if (k != i) {
                double factor = matrix[k][i];
                for (int j = 0; j < n; ++j) {
                    matrix[k][j] -= factor * matrix[i][j];
                    inverse[k][j] -= factor * inverse[i][j];
                }
            }
        }
    }
    return true;
}

int main() {
    int n;
    cin >> n;

    vector<vector<double> > matrix(n, vector<double>(n));
    vector<vector<double> > inverse(n, vector<double>(n));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> matrix[i][j];

    if (getInverse(matrix, inverse, n)) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j)
                cout << inverse[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << -1 << endl; 
    }
    return 0;
}
