#include <iostream>

int main()
{
    int N;
    std::cin >> N;
    int ans = 1 << N;
    std::cout << (ans + 1) * (ans + 1);
    
    return 0;
}