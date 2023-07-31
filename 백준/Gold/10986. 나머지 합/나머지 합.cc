#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long n, m;
    cin >> n >> m;

    long *a, *b;
    a = new long[n + 1]();
    b = new long[n + 1]();

    for(int i = 1; i <= n; i ++) {
        long temp;
        cin >> temp;
        a[i] = (a[i - 1] + temp) % m;
        b[a[i]]++;
    }

    long ans = 0;
    ans += b[0];
    for(int i = 0; i < n + 1; i++) {
        if(b[i] != 0) {
            ans += (b[i] * (b[i] - 1)) / 2;
        }
    }
    
    cout << ans << endl;

    delete [] a;
    delete [] b;
}