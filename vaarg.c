
#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void variadic (const char *str, ...);
int ft_match(const char **content);


int main()
{
    const char * str = "hello, [] player(s) connected to [] host(s).\n";
    variadic(str, 2, 4);

    return (0);
}


void variadic (const char *content, ...)
{
    va_list ptr;
    va_start(ptr, content);
    char nbr;
    while (*content)
    {
        if (ft_match(&content))
        {
            nbr = va_arg(ptr,int) + '0';
            write(1,&nbr,1);
        }
        write(1,content++,1);
    }
}

int ft_match(const char **content)
{
    while (strncmp((*content),"[]",2) == 0)
    {
        (*content) += 2;
        return (1);
    }
    return (0);
}