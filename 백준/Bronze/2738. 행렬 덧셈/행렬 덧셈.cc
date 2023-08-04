#include <iostream>

int A[101][101] = {0};
int B[101][101] = {0};

int main()
{
    int N, M;
    std::cin >> N >> M;
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<M; j++)
        {
            int temp;
            std::cin >> temp;
            A[i][j] = temp;
        }
    }
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<M; j++)
        {
            int temp;
            std::cin >> temp;
            B[i][j] = temp;
        }
    }
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<M; j++)
        {
            std::cout << A[i][j] + B[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}