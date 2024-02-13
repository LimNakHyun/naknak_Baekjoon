#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, vector<int> slicer, vector<int> num_list)
{
    int start = 0;
    int end = slicer[1];
    int gap = 1;
    
    if(n == 2)
    {
        start = slicer[0];
        end = num_list.size() - 1;
    }
    else if(n == 3)
    {
        start = slicer[0];
        end = slicer[1];
    }
    else if(n == 4)
    {
        start = slicer[0];
        end = slicer[1];
        gap = slicer[2];
    }
    
    vector<int> answer;
    for(int i=start; i<=end; i=i+gap)
    {
        answer.push_back(num_list[i]);
    }
    
    return answer;
}