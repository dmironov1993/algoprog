//https://algoprog.ru/material/p973

#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n == 1)
        return false;
    int i = 2;
    while (i*i <= n) {
        if (n % i == 0)
            return false;
        i += 1;
    }
    return true;
}

int main() {
    int k;
    cin >> k;
    int cnt = 0, j = 2;
    while (true) {
        if (is_prime(j))
            cnt++;
        if (cnt == k)
            break;
        j++;
    }
    cout << j << endl;
    return 0;
}
