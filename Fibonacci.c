#include<stdio.h>int l(int n){return n<2?n:l(n-1)+l(n-2);}int main(){for(int i=0;i<31;i++)printf("%d\n",l(i));return 0;}
