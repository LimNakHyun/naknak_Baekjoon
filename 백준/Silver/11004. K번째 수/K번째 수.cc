#include <iostream>

int A[5000000];

void swap(int A[], int i, int j)
{
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

int partition(int A[], int S, int E, int size)
{
    if (S+1 == E)
    {
        if (A[S] > A[E])
        {
            swap(A, S, E);
        }
        return E;
    }
    
    int M = (S + E) / 2;
    swap(A, S, M);
    int pivot = A[S];
    int i = S + 1, j = E;
    
    while (i <= j)
    {
        while (pivot < A[j] && j > 0)
        {
            j--;
        }
        while (pivot > A[i] && i < size - 1)
        {
            i++;
        }
        if (i <= j)
        {
            swap(A, i++, j--);
        }
    }
    A[S] = A[j];
    A[j] = pivot;
    return j;
}

void quickSort(int A[], int S, int E, int K, int size)
{
    int pivot = partition(A, S, E, size);
    if (pivot == K)
    {
        return;
    }
    else if (K < pivot)
    {
        quickSort(A, S, pivot-1, K, size);
    }
    else
    {
        quickSort(A, pivot+1, E, K, size);
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int N, K;
    std::cin >> N >> K;
    
    for (int i=0; i<N; i++)
    {
        std::cin >> A[i];
    }
    
    quickSort(A, 0, N - 1, K - 1, N);
    
    std::cout << A[K-1];
    
    return 0;
}