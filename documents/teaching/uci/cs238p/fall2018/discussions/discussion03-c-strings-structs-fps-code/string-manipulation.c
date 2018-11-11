#include <stdio.h>


void myfun(char * a, char * b){
  while (*a++ = *b++);
}

void main(int argc, char* argv[]){

    // Successful:
    // printf("Your string 1: %s\n",argv[1]);
    // printf("Your string 2: %s\n",argv[2]);
    // myfun(argv[1],argv[2]);
    // printf("After myfun, string 1 is %s\n", argv[1]);
    // printf("After myfun, string 2 is %s\n", argv[2]);

    // You can't do this - 1:
    // char * str1 = "abc";
    // char * str2 = "bbc";
    // printf("Your string 1: %s\n",str1);
    // printf("Your string 2: %s\n",str2);
    // myfun(str1,str2);//can't change strings
    
    // You also can't do this - 2:
    // char *strings[2]={
    //     [0]="abc",
    //     [1]="bbc"
    //     };
    // printf("Your string 1: %s\n",strings[0]);
    // printf("Your string 2: %s\n",strings[1]);
    // myfun(strings[0],strings[1]);//can't change strings

    // You also can't do this - 3:
    // char *strings[2]={"abc","def"};
    // printf("Your string 1: %s\n",strings[0]);
    // printf("Your string 2: %s\n",strings[1]);
    // printf("5th element: %c\n",*(strings[0]+5));
    // *(strings[0])='x'; //can't change strings
    // myfun(strings[0],strings[1]);//can't change strings

    //This works - Works !:
    char a[] = "abc";
    char b[] = "def";
    char *strings[2]={
        [0]=a,
        [1]=b
        // [0]="abc",//[later]storing in this way we get contiguous
        // [1]="def"
        };

    // //check contiguity[later]
    // printf("0th element address: %p\n",strings[0]);
    // printf("1st element address: %p\n",strings[1]);

    printf("Your string 1: %s\n",strings[0]);
    printf("Your string 2: %s\n",strings[1]);
    myfun(strings[0],strings[1]);
    printf("After myfun, string 1 is %s\n", strings[0]);
    printf("After myfun, string 2 is %s\n", strings[1]);
}

//Reference:

//Scanf Format Specifiers
//https://www.tutorialspoint.com/c_standard_library/c_function_scanf.htm
//"After the first arg of scanf, there can be multiple 
//scanf arguments - there should be the same number of these arguments as the number of 
//%-tags that expect a value."

//Initial value of pointers
//https://stackoverflow.com/questions/7240365/pointer-default-value

// K & R - C 2nd Edition:

// "There is an important difference between these definitions:
// char amessage[] ="asdf";
// char *pmessage = "asdf";

// amessaqe is an array, just big enough to hold the sequence of characters and
// ,\0' that initializes it. Individual characters within the array may be changed
// but amessaqe will always refer to the same storage. 

// On the other hand,
// pmessaqe is a pointer, initialized to point to a string constant; the pointer may
// subsequently be modified to point elsewhere, but the result is undefined if you
// try to modify the string contents."
