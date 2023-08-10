#include <iostream>

int A[1000001];
int tmp[1000001];   // 정렬 시 잠시 사용할 임시 배열 선언

void merge_sort(int s, int e)
{
    if (e-s < 1)
    {
        return;
    }
    
    int m = s + (e - s) / 2;
    
    // 재귀 함수 형태로 구현
    merge_sort(s, m);
    merge_sort(m+1, e);
    
    for (int i=s; i<=e; i++)
    {
        tmp[i] = A[i];
    }
    
    int k = s;
    int index1 = s;
    int index2 = m + 1;
    
    while (index1 <= m && index2 <= e)
    {
        if (tmp[index1] > tmp[index2])
        {
            A[k] = tmp[index2];
            k++;
            index2++;
        }
        else
        {
            A[k] = tmp[index1];
            k++;
            index1++;
        }
    }
    // 한쪽 그룹이 모두 선택된 후 남아있는 값 정리하기
    while (index1 <= m)
    {
        A[k] = tmp[index1];
        k++;
        index1++;
    }
    while (index2 <= e)
    {
        A[k] = tmp[index2];
        k++;
        index2++;
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int N;
    std::cin >> N;
    for (int i=1; i<N+1; i++)
    {
        std::cin >> A[i];
    }
    
    merge_sort(1, N);
    
    for (int i=1; i<=N; i++)
    {
        std::cout << A[i] << "\n";
    }

    return 0;
}