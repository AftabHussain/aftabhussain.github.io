#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MSG1 "quick"
#define MSG2 "brown"
#define MSG3 "fox"


static char* text_array[3]= {MSG1, MSG2, MSG3};

int main(int argc, char *argv[]){

 printf("%c\n",*(text_array[0]+5));

 printf("%p\n",text_array[0]);

 return 0;
}

/***REFERENCES***/
/*
1. main function specification
https://en.cppreference.com/w/cpp/language/main_function
2. printf format specifiers 
http://www.cplusplus.com/reference/cstdio/printf/
*/
