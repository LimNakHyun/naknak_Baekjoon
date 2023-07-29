#include <iostream>

int A[101];

int main()
{
    int N, M;
    std::cin >> N >> M;
    
    for (int a=0; a<M; a++)
    {
        int i, j, k;
        std::cin >> i >> j >> k;
        for (int b=i; b<=j; b++)
        {
            A[b] = k;
        }
    }
    
    for (int i=1; i<=N; i++)
    {
        std::cout << A[i] << " ";
    }
    
    return 0;
}