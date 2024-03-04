#include <iostream>

int A[20000001];

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int N, M, card, count;
    std::cin >> N;
    for(int i=0; i<N; i++)
    {
        std::cin >> card;
        A[card + 10000000]++;
    }

    std::cin >> M;
    for(int i=0; i<M; i++)
    {
        std::cin >> count;
        std::cout << A[count + 10000000] << " ";
    }

    return 0;
}