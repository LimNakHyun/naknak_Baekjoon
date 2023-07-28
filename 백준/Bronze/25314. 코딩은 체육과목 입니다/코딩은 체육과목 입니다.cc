#include <iostream>

using namespace std;

int main()
{
    int N;      // 바이트값
    cin >> N;
    
    for (int i=0; i<N / 4; i++)
    {
        cout << "long" << " ";
    }
    cout << "int";

    return 0;
}