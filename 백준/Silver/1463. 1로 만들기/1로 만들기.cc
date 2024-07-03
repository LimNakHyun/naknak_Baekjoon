#include <iostream>
#include <vector>

static int N, ANS;
static std::vector<int> D;
int count_operation(int n);

int main()
{
    std::cin >> N;
    D.resize(N+1);

    for(int i=0; i<N+1; i++)
    {
        D[i] = -1;
    }
    D[0] = 0;
    D[1] = 0;

    ANS = count_operation(N);

    std::cout << ANS;
}

int count_operation(int n)
{
    for(int i=1; i<N; i++)
    {
        int count = D[i];
        
        if(i+1 < N+1 && (D[i+1] == -1 || D[i+1] > count+1))
        {
            D[i+1] = count+1;
        }

        if(i*2 < N+1 && (D[i*2] == -1 || D[i*2] > count+1))
        {
            D[i*2] = count+1;
        }

        if(i*3 < N+1 && (D[i*3] == -1 || D[i*3] > count+1))
        {
            D[i*3] = count+1;
        }
    }

    return D[N];
}