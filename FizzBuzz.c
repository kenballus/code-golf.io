#include <stdio.h>int main(){for(int j=1;j<101;j++){const char*a=j%3?"":"Fizz";const char*b=j%5?"":"Buzz";char s[4];sprintf(s,"%d",j);printf("%s%s%s\n",a,b,(a[0]||b[0])?"":s);}return 0;}
