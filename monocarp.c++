
#include <iostream>

int main()
{
    short n, k, d , i ,tmp;
    short t;
    
    i = 1; 
    std::cin >> t; 
    while (t--)
    {
        std::cin >> n; 
        std::cin >> k; 
        
        d = n-k;
        tmp = d;
        while (d >= i)
        {
            std::cout << d << " ";
            d--;
        }
        while (tmp < n)
        {
            tmp++;
            std::cout << tmp << " ";
        }
        std::cout << std::endl;
    }
}