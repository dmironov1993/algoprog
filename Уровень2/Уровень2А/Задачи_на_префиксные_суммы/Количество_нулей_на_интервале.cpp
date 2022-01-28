// https://algoprog.ru/material/p3313

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    int array[n][m];
    for (auto i = 0; i < n; i++) {
        for (auto j = 0; j < m; j++) {
            int tmp;
            cin >> tmp;
            array[i][j] = tmp;
        }
    }
    int prefix[n][m];
    for (auto i = 0; i < n; i++) {
        for (auto j = 0; j < m; j++) {
            if (i == 0 and j == 0) {
                prefix[i][j] = array[i][j];
            } else if (i >= 1 and j == 0) {
                prefix[i][j] = array[i][j] + prefix[i-1][m-1];
            } else {
                prefix[i][j] = array[i][j] + prefix[i][j-1];
            }
        }
    }
    for (auto j = 0; j < k; j++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        x1--;
        y1--;
        x2--;
        y2--;
        int cnt = 0;
        for (auto i = x1; i < x2 + 1; i++) {
            if (i == 0 and y1 == 0) {
                cnt += prefix[i][y2];
            } else if (i >= 1 and y1 == 0) {
                cnt += prefix[i][y2] - prefix[i-1][m-1];
            } else {
                cnt += prefix[i][y2] - prefix[i][y1-1];
            }
        }
        cout << cnt << endl;
    }
    return 0;
}
