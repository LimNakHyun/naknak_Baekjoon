#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b)
{
    string str_a = to_string(a);
    string str_b = to_string(b);
    
    return (str_a + str_b) > (str_b + str_a);
}

string solution(vector<int> numbers)
{
    string answer = "";
    int N = numbers.size();
    
    sort(numbers.begin(), numbers.end(), compare);
    
    for (int i=0; i<N; i++)
    {
        if (answer == "0")
        {
            answer = "";
        }
        answer += to_string(numbers[i]);
    }
    
    return answer;
}