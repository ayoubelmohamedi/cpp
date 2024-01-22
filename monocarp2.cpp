#include <iostream>

int main(){

	short t;

	std::cin >> t;
	while (t--)
	{
		short n;
		short k;

		std::cin >> n >> k;
		short s = n - k;
		short _s = s;
		short i = 0;
		while(i < n)
		{
			if (s >= 1)
			{
				std::cout << s-- <<" ";
			}else if (s == 0)
			{
				std::cout <<++_s << " ";
			}else
			{
				break;
			}
			i++;
		}


	}

}