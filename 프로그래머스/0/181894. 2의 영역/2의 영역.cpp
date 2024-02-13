#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr)
{
    int start = -1;
    int end = -1;
    
    for(int i=0; i<arr.size(); i++)
    {
        if(arr[i] == 2)
        {
            if(start == -1)
                start = i;
            else
                end = i;
        }
    }
    
    vector<int> answer;
    
    if(start == -1)
        answer.push_back(-1);
    else if(end == -1)
        answer.push_back(2);
    else
    {
        end++;
        for(int i = start; i < end; i++)
            answer.push_back(arr[i]);
    }
    
    return answer;
}