#include<stdio.h>
int n,m,r,main(){for(n=1;n<1001;n++){for(r=0,m=n;m>1;r++){m=m%2?m*3+1:m/2;}printf("%d\n",r);}}
