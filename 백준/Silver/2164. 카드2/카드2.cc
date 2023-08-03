#include <iostream>
#include <queue>

int main()
{
    int N;
    std::cin >> N;
    
    std::queue<int> Q;
    
    for (int i=1; i<=N; i++)
    {
        Q.push(i);
    }
    
    while (Q.size() > 1)
    {
        Q.pop();
        int temp = Q.front();
        Q.pop();
        Q.push(temp);
    }
    
    std::cout << Q.front();
    
    return 0;
}