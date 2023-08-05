#include <iostream>

int main()
{
    int T;
    std::cin >> T;
    
    for (int i=0; i<T; i++)
    {
        std::string str;
        std::cin >> str;
        std::cout << str[0] << str[str.size()-1] << '\n';
    }
    
    return 0;
}