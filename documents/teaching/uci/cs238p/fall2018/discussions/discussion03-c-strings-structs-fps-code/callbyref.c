//source: https://www.tutorialspoint.com/cprogramming/c_function_call_by_reference.htm

#include <stdio.h>
 
/* function declaration */
void swap(int *x, int *y) {

   int temp;
   temp = *x;    /* save the value at address x */
   *x = *y;      /* put y into x */
   *y = temp;    /* put temp into y */
  
   return;
}
 
int main () {

   int *a ;
   int *b ;

   // *a = 100; you can't do this at this stage! need to initialize the pointers!
   // *b = 200;

   int val1 = 100;
   int val2 = 200; 

   a = &val1;
   b = &val2;

   printf("Before swap, value of a : %d\n", *a );
   printf("Before swap, value of b : %d\n", *b );
 
   /* calling a function to swap the values.
      * &a indicates pointer to a ie. address of variable a and 
      * &b indicates pointer to b ie. address of variable b.
   */
   swap(a, b);
 
   printf("After swap, value of a : %d\n", *a );
   printf("After swap, value of b : %d\n", *b );
 
   return 0;
}

//Reference:
// why you cannot directly assign pointer (there are exceptions)
//https://stackoverflow.com/questions/17665793/directly-assigning-values-to-c-pointers
