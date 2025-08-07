#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(n));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> matrix[i][j];

    int d1 = 0, d2 = 0;

    for (int i = 0; i < n; ++i) {
        d1 += matrix[i][i];
        d2 += matrix[i][n - 1 - i];
    }

    cout << abs(d1 - d2) << endl;

    return 0;
}
