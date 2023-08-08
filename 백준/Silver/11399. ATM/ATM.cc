#include <iostream>

int A[1000];

int main()
{
    int N;
    std::cin >> N;
    
    for (int i=0; i<N; i++)
    {
        std::cin >> A[i];
    }
    
    for (int i=1; i<N; ++i)
    {
        int key = A[i];
        int j = i - 1;
        
        while (j >= 0 && A[j] > key)
        {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = key;
    }
    
    int ans = 0;
    for (int i=1; i<N+1; i++)
    {
        for (int j=0; j<i; j++)
        {
            ans += A[j];
        }
    }
    
    std::cout << ans;

    return 0;
}