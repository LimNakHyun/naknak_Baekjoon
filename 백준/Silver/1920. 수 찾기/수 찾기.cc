#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int N, M;
    std::cin >> N;
    std::vector<int> A(N, 0);
    
    for (int i=0; i<N; i++)
    {
        std::cin >> A[i];
    }
    
    std::sort(A.begin(), A.end());
    
    std::cin >> M;
    for (int i=0; i<M; i++)
    {
        int start_idx = 0, end_idx = N-1;
        int median_idx = (start_idx + end_idx) / 2;
        
        int temp;
        std::cin >> temp;
        
        while (start_idx <= end_idx)
        {
            if (temp > A[median_idx])
            {
                start_idx = median_idx+1;
            }
            else if (temp < A[median_idx])
            {
                end_idx = median_idx-1;
            }
            else    // temp == A[median_idx]
            {
                break;
            }
            median_idx = (start_idx + end_idx) / 2;
        }
        
        if (temp == A[median_idx])
        {
            std::cout << 1 << "\n";
        }
        else
        {
            std::cout << 0 << "\n";
        }
    }

    return 0;
}