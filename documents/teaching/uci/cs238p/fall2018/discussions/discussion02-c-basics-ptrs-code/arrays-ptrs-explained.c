#include<stdio.h>
#include<stdlib.h>

static int a[] = {97,46,45,88};

int main(int argc, char *argv[]){
    int *p;

    p=a;
    //the array name a, is converted into a pointer, in the above statement
    //points to the first element of the array.
    //https://stackoverflow.com/questions/1641957/is-an-array-name-a-pointer

    p = &a[0];
    //the same as above, 
    //p points to the first element of the array. 

    printf("pointer p's value %p\n",p);
    p+=1;//p is incremented by 1.
    printf("pointer p's value after increment %p\n",p);

    printf("*p is %d\n",*p);
    printf("p[0] is %d\n\n",p[0]); //So, p[0] is the same as *p

    printf("p[-1] is %d\n\n",p[-1]); //you can use negative indices to access locations

    printf("*--p is %d\n\n",*--p); //p is decremented, then dereferenced.

    // p = &a;
    //this would send a warning. Here, again a is converted into a pointer, 
    //and we are assigning the address of a to q -- but their types are different. more on this below

    /**&a and a**/

    printf("a %p\n",a);
    printf("&a %p\n\n",&a);

    printf("a+1 %p\n",a+1);
    printf("&a+1  %p\n",&a+1);
    //while they are both pointers their types are different
    //one is of the array element type, and one is of the array type 
    //itself
    //take help of https://www.calculator.net/hex-calculator.html?number1=601060&c2op=-&number2=601050&calctype=op&x=76&y=25
    // to get byte differences


 return 0;
}

