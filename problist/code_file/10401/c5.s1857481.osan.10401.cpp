#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int main()
{

    vector<int> str;
    int times;
    int num;
    int p[40] = {0,1};
    for(int i=2;i<40;i++){
        p[i]=p[i-1]+p[i-2];
    }


    cin>>times;
    for(int i=0;i<times;i++){
        cin>>num;
        cout<<num<<" = ";
        int flag=39;
        while(p[flag]>num){
            flag--;
        }

        for(int j=flag;j>=2;j--){
            if(num >= p[j]){
                cout<<'1';
                num = num-p[j];
            }
            else
                cout<<'0';


        }
        cout<<" (fib)"<<endl;

    }
    return 0;
}
