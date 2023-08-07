#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int N;
    std::cin >> N;
    std::vector<std::pair<int, int>> A(N);
    
    for (int i=0; i<N; i++)
    {
        std::cin >> A[i].first;
        A[i].second = i;
    }
    
    std::sort(A.begin(), A.end());
    
    int maxIdx = -1;
    for (int i=0; i<N; i++)
    {
        if (A[i].second - i > maxIdx)
        {
            maxIdx = A[i].second - i;
        }
    }
    std::cout << maxIdx + 1;

    return 0;
}