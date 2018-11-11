#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MSG1 "quick"
#define MSG2 "brown"
#define MSG3 "fox"

//giving the number of params is optional.
static char* text_array[3]= {MSG1, MSG2, MSG3};

int main(int argc, char *argv[]){

 printf("%c\n",*(text_array[0]+6));//prints char at address + 6: there is a null character after each string occupying a cell.

 printf("%p\n",text_array[0]);//prints the first element of text_array (an address) --> this address changes with every run.

 char * p = (char*)0x400604;
 printf("%c\n",*p);//prints the character at this address
 
 int total_msg_arr_bytes;
 
 for (int i=0; i < 3; i++){
     total_msg_arr_bytes+= (int)strlen(text_array[i])+1;
 }

 printf("printing all the messages\n");

 for (int i=0; i < total_msg_arr_bytes; i++){

  if (*(text_array[0]+i)=='\0'){//to avoid the problem below
   printf("Null\n");
   continue;
  }
                                    
   if (*(text_array[0]+i)=='\0'){ //a better practice to handle the null pointer
   printf("%c\n",*(text_array[0]+i));//make sure you don't dereference Null!

   printf("%p\n",text_array[0]+i);
 }

 return 0;
}

/***REFERENCES***/
/*
1. main function specification
https://en.cppreference.com/w/cpp/language/main_function
2. printf format specifiers 
http://www.cplusplus.com/reference/cstdio/printf/





*/
