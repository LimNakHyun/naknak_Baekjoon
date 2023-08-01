#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int N;
    std::cin >> N;
    std::vector<int> A;

    for (int i=0; i<N; i++)
    {
        int temp;
        std::cin >> temp;
        A.push_back(temp);
    }

    std::sort(A.begin(), A.end());

    int start_idx = 0, end_idx = N - 1, ans = 0;
    for (int i=0; i<N; i++)
    {
        while (start_idx < end_idx)
        {
            if (A[start_idx] + A[end_idx] == A[i])
            {
                if (start_idx != i && end_idx != i)
                {
                    ans++;
                    break;
                }
                else if (start_idx == i)
                {
                    start_idx++;
                }
                else if (end_idx == i)
                {
                    end_idx--;
                }
            }
            else if (A[start_idx] + A[end_idx] > A[i])
            {
                end_idx--;
            }
            else    // A[start_idx] + A[end_idx] < A[i]
            {
                start_idx++;
            }
        }
        start_idx = 0;
        end_idx = N - 1;
    }
    std::cout << ans;
    
    return 0;
}

