#include<stdio.h>int main(){for(int j=2;j<98;j++){int a=1;for(int i=2;i<j;i++){if(j%i<1)a=0;}if(a>0)printf("%i\n",j);}return 0;}
