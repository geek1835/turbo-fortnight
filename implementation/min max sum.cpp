#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{int i; long long a[5],b[5];
long long  sum =0;long long max,min;
for(i=0;i<5;i++)
{

cin>>a[i];
sum+=a[i];

}

for(i=0;i<5;i++)
{
	b[i]=sum-a[i];

}

max=min=b[0];
for(i=0;i<5;i++)
{
	if(b[i]>max)
	max=b[i];
	if(b[i]<min)
	min=b[i];	
	
}
cout<<min<<" "<<max;

return 0;
}
