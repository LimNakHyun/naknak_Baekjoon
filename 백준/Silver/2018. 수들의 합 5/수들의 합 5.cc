#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    int c = sqrt(n) + 2000;
    int ans = 0;
    for(int i = 1; i < (n / 2) + 2000; i++) {
        while((c * (2 * i + (c - 1))) > n * 2) c--;
        if((c * (2 * i + (c - 1))) == n * 2) {
            ans++;
            if(i == n) ans--;
        }
    }

    cout << ans + 1;
}