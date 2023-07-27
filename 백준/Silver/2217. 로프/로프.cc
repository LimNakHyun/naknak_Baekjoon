#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    cin >> N;
    
    int max = 0;
    vector<int> ropes;
    
    for (int i=0; i<N; i++)
    {
        int rope;
        cin >> rope;
        ropes.push_back(rope);
    }
    sort(ropes.begin(), ropes.end());
    
    for (int i=0; i<N; i++)
    {
        if (max < ropes[i] * (N - i))
        {
            max = ropes[i] * (N - i);
        }
    }
    cout << max;
    
    return 0;
}