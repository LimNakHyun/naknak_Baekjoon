#include <iostream>

int A[101];

int main()
{
    int N, M;
    std::cin >> N >> M;
    
    for (int i=0; i<=N; i++)
    {
        A[i] = i;
    }
    
    for (int k=0; k<M; k++)
    {
        int i, j;
        std::cin >> i >> j;
        
        int* B = new int[j-i+1];
        int idx = 0;
        for (int l=i; l<=j; l++)
        {
            B[idx++] = A[l];
        }
        
        for (int l=i; l<=j; l++)
        {
            A[l] = B[--idx];
        }
        
        delete[] B;
    }
    
    for (int i=1; i<=N; i++)
    {
        std::cout << A[i] << " ";
    }
    
    return 0;
}

