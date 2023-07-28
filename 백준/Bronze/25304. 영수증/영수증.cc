#include <iostream>

using namespace std;

int main()
{
    int X, N, price = 0;      // 영수증에 적힌 총 금액 X, 구매한 물건의 종류 N, 물건 가격을 모두 더한 price
    cin >> X >> N;
    
    for (int i=0; i<N; i++)
    {
        int a, b;
        cin >> a >> b;
        price += a * b;
    }
    
    if (X == price) cout << "Yes";
    else cout << "No";

    return 0;
}
