#include <iostream>
#include <vector>
using namespace std;

void getREF(vector<vector<double> > &matrix, int m, int n) {
    for (int i = 0; i < m; ++i) {
        if (matrix[i][i] == 0) {
            for (int j = i + 1; j < m; ++j) {
                if (matrix[j][i] != 0) {
                    swap(matrix[i], matrix[j]);
                    break;
                }
            }
        }
        for (int j = i + 1; j < m; ++j) {
            double factor = matrix[j][i] / matrix[i][i];
            for (int k = 0; k < n; ++k) {
                matrix[j][k] -= factor * matrix[i][k];
            }
        }
    }
}

int main() {
    int m, n;
    cin >> m >> n;

    vector<vector<double> > matrix(m, vector<double>(n));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    getREF(matrix, m, n);

    for (int i = 0; i < m; ++i) {  
        for (int j = 0; j < n; ++j) { 
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
