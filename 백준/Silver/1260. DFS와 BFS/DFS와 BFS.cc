#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

static std::vector<std::vector<int>> A;
static std::vector<int> B;
static std::queue<int> Q;

void DFS(int i)
{
    if (B[i] == 1)
    {
        return;
    }
    
    B[i] = 1;
    std::cout << i << " ";
    
    for (int j: A[i])
    {
        if (B[j] == 0)
        {
            DFS(j);
        }
    }
}

int main()
{
    int N, M, V;
    std::cin >> N >> M >> V;
    
    A.resize(N+1);
    B = std::vector<int>(N+1, 0);
    
    for (int i=0; i<M; i++)
    {
        int u, v;
        std::cin >> u >> v;
        A[u].push_back(v);
        A[v].push_back(u);
    }
    
    for (auto& temp: A)
    {
        std::sort(temp.begin(), temp.end());
    }
    
    DFS(V);
    std::cout << std::endl;
    
    fill(B.begin(), B.end(), 0);
    
    Q.push(V);
    B[V] = 1;
    while (!Q.empty())
    {
        int temp = Q.front();
        Q.pop();
        for (int i: A[temp])
        {
            if (B[i] == 0)
            {
                B[i] = 1;
                Q.push(i);
            }
        }
        std::cout << temp << " ";
    }

    return 0;
}