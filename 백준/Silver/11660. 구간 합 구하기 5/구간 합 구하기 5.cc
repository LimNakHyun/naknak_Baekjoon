#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, m;
    cin >> n >> m;

    int **a;
    a = new int*[n + 1]();
    for(int i = 0; i < n + 1; i++) {
        a[i] = new int[n + 1]();
    }

    for(int i = 1; i < n + 1; i++) {
        for(int j = 1; j < n + 1; j++) {
            int temp;
            cin >> temp;
            a[i][j] = a[i - 1][j] + a[i][j - 1] + temp - a[i - 1][j - 1];
        }
    }

    for(int i = 0; i < m; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << a[x2][y2] - (a[x1 - 1][y2] + a[x2][y1 - 1]) + a[x1 - 1][y1 - 1] << "\n"; 
    }

    for(int i = 0; i < n + 1; i++) {
        delete [] a[i];
    }
    delete [] a;
}