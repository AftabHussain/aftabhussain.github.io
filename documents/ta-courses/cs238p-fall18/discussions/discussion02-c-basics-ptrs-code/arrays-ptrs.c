#include<stdio.h>
#include<stdlib.h>

static int a[] = {97,46,45,88};

int main(int argc, char *argv[]){
    int *p;

    p=a;




    p = &a[0];



    printf("pointer p's value %p\n",p);
    p+=1;
    printf("pointer p's value after increment %p\n",p);

    printf("*p is %d\n",*p);
    printf("p[0] is %d\n\n",p[0]); 

    printf("p[-1] is %d\n\n",p[-1]);

    printf("*--p is %d\n\n",*--p);





    /**&a and a**/

    printf("a %p\n",a);
    printf("&a %p\n\n",&a);

    printf("a+1 %p\n",a+1);
    printf("&a+1  %p\n",&a+1);







 return 0;
}

