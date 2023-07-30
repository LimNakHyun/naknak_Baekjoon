#include <iostream>

int A[101];

int main()
{
    int N, M;
    std::cin >> N >> M;
    
    for (int i=0; i<N+1; i++)
    {
        A[i] = i;
    }
    
    for (int a=0; a<M; a++)
    {
        int i, j, temp;
        std::cin >> i >> j;
        temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
    
    for (int i=1; i<=N; i++)
    {
        std::cout << A[i] << " ";
    }
    
    return 0;
}