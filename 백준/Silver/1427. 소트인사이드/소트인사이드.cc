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
        int maxIdx = i+1;
        for (int j=i+1; j<str.size(); j++)
        {
            if (A[j] > A[maxIdx])
            {
                maxIdx = j;
            }
        }
        if (A[maxIdx] > A[i])
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
