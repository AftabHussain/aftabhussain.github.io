#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MSG1 "quick"
#define MSG2 "brown"
#define MSG3 "fox"


static char* text_array[3]= {MSG1, MSG2, MSG3};

int main(int argc, char *argv[]){

 printf("%c\n",*(text_array[0]+6));

 printf("%p\n",text_array[0]);



 return 0;
}


