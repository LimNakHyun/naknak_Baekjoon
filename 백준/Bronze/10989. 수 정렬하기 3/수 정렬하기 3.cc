#include <iostream>

int A[10001];

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int N;
    std::cin >> N;
    
    for (int i=0; i<N; i++)
    {
        int temp;
        std::cin >> temp;
        A[temp]++;
    }
    
    for (int i=1; i<10001; i++)
    {
        while (A[i] > 0)
        {
            std::cout << i << "\n";
            A[i]--;
        }
    }

    return 0;
}