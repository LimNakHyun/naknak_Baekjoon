#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int max = -1, col = 0, row = 0;

    vector<vector<int>> A(10, vector<int>(10));

    for(int i=0; i<9; i++)
    {
        for(int j=0; j<9; j++)
        {
            int temp;
            cin >> temp;
            if(temp > max)
            {
                max = temp;
                row = i + 1;
                col = j + 1;
            }
        }
    }

    cout << max << endl;
    cout << row << " " << col << endl;

}