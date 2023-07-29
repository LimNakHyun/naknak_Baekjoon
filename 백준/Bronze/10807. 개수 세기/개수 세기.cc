#include <iostream>

int A[201];

int main()
{
    int N, num, v;
    std::cin >> N;
    
    for (int i=0; i<N; i++)
    {
        std::cin >> num;
        A[num + 100]++;
    }
    
    std::cin >> v;
    std::cout << A[v + 100];
    
    return 0;
}