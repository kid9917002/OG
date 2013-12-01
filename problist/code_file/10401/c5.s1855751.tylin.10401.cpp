#include <iostream>
#include <vector>
using namespace std;

int main(){
    int round;
    vector<int> ftable;
    int fsum = 3;
    int i;


    ftable.push_back(1);
    ftable.push_back(2);
    for(i=2;fsum<100000000;i++){
        ftable.push_back(ftable[i-1]+ftable[i-2]);
        fsum = ftable[i];
    }

    cin>>round;

    int dec;
    int ans=0;

    while(round--){
        cin>>dec;
        cout<<dec<<" = ";
        ans=0;
        for(i=ftable.size()-1;i>=0;i--){
            if(ftable[i]<=dec){
                dec -= ftable[i];
                ans = ans | (1<<i);
            }
        }
        int flag = 0;
        for(i=31;i>=0;i--){
            if(ans & (1<<i)){
                if(flag == 0)
                    flag = 1;
                cout<<"1";
            }else{
                if(flag ==1)
                    cout<<"0";
            }
        }
        cout<<" (fib)"<<endl;
    }
}
