#https://algoprog.ru/material/p2771

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> array;
    for (auto i = 0; i < n; i++) {
        int t;
        cin >> t;
        array.push_back(t);
    }
    vector<int> prefix;
    prefix.push_back(0);
    for (auto i = 1; i < n + 1; i++) {
        prefix.push_back(prefix[i-1] + array[i-1]);
    }
    for (auto k = 0; k < m; k++) {
        int i, j;
        cin >> i >> j;
        cout << prefix[j] - prefix[i-1] << endl;
    }
    return 0;
}
