#include <iostream>

int A[1001];

int main()
{
    int N;
    std::cin >> N;
    
    for (int i=0; i<N; i++)
    {
        int num;
        std::cin >> num;
        A[i] = num;
    }
    
    for (int i=0; i<N-1; i++)
    {
        for (int j=i+1; j<N; j++)
        {
            if (A[i] > A[j])
            {
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
    }
    
    for (int i=0; i<N; i++)
    {
        std::cout << A[i] << '\n';
    }

    return 0;
}