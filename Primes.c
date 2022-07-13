#include<stdio.h>int i,j,a,main(){for(j=2;j<98;j++){a=1;for(i=2;i<j;i++){if(j%i<1)a=0;}if(a>0)printf("%i\n",j);}}
