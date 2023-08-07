#include <iostream>

int A[10];

int main()
{
    std::string str;
    std::cin >> str;
    
    for (int i=0; i<str.size(); i++)
    {
        A[i] = str[i] - '0';
    }
    
    for (int i=0; i<str.size(); i++)
    {
        int max = -1;
        int maxIdx;
        for (int j=i+1; j<str.size(); j++)
        {
            if (A[j] > max)
            {
                max = A[j];
                maxIdx = j;
            }
        }
        if (max > A[i])
        {
            int temp = A[maxIdx];
            A[maxIdx] = A[i];
            A[i] = temp;
        }
    }
    
    for (int i=0; i<str.size(); i++)
    {
        std::cout << A[i];
    }

    return 0;
}
