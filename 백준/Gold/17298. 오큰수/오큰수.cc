#include <iostream>
#include <stack>
typedef std::pair<int, int> Node;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    std::stack<Node> stk;

    int A;  // 수열의 크기 A
    std::cin >> A;

    int* ans = new int[A] {0,};

    for (int i=0; i<A; i++)
    {
        int now;
        std::cin >> now;
        if (stk.empty())
        {
            stk.push(Node(i, now));
        }
        else
        {
            int temp_top = stk.top().second;
            if (now > temp_top)
            {
                while (now > temp_top)
                {
                    ans[stk.top().first] = now;
                    stk.pop();
                    if (stk.empty()) break;
                    else temp_top = stk.top().second;
                }
            }
            stk.push(Node(i, now));
        }
    }

    for (int i=0; i<A; i++)
    {
        if (ans[i] != 0)
        {
            std::cout << ans[i] << " ";
        }
        else
        {
            std::cout << -1 << " ";
        }
    }

    delete[] ans;

    return 0;
}