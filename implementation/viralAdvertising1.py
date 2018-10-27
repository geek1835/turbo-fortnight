#include <bits/stdc++.h>

using namespace std;

// Complete the viralAdvertising function below.
int viralAdvertising(int n) {
    int like=0,sum,share=5,x=0;
    for(int i=1;i<=n;i++)
    {
     sum=like+share/2;
        share=(share/2)*3;
        x=x+sum;
    }
    return x;


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = viralAdvertising(n);

    fout << result << "\n";

    fout.close();

    return 0;
}
