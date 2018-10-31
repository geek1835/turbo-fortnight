#include <bits/stdc++.h>

using namespace std;


int main() {
    int t,k,i,x=0;
    cin >> t; int n;   int y;
while(t--)
{
        cin >> n >> k;
   
    for(i=0;i<n;i++)
    {
        cin>>y;
  
        if(y<=0)
            x++;
    } 
    if(x>=k)
        cout<<"NO"<<endl;
    else
        cout<<"YES"<<endl;
    x=0;
   
    }
    return 0;
}
