#include <iostream>
#include <vector>

static std::vector<std::vector<int>> A;
static std::vector<int> B;

void DFS(int i)
{
    if (B[i])
    {
        return;
    }
    
    B[i] = 1;
    
    for (int j: A[i])
    {
        if (!B[j])
        {
            DFS(j);
        }
    }
}

int main()
{
    int N, M;
    std::cin >> N >> M;
    
    A.resize(N+1);
    B = std::vector<int>(N+1, 0);
    
    for (int i=0; i<M; i++)
    {
        int u, v;
        std::cin >> u >> v;
        A[u].push_back(v);
        A[v].push_back(u);
    }
    
    int ans = 0;
    for (int i=1; i<N+1; i++)
    {
        if (!B[i])
        {
            ans++;
            DFS(i);
        }
    }
    std::cout << ans;
    
    return 0;
}