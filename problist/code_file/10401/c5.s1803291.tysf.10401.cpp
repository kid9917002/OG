/*
http://gpe2.acm-icpc.tw/showproblemtab.php?probid=10401&cid=5
*/
#include <iostream>

using namespace std;

int main()
{
    int que[40]={0,1};
    for(int i = 2 ; i < 40 ; i++)
        que[i] = que[i-1] + que[i-2];
    int N , input;
    bool check;
    cin >> N;
    while(N--){
        cin >> input;
        cout << input << " = ";
        check = false;
        for(int i = 39 ; i >= 2 ; i--){
            if(input >= que[i]){
                cout << "1";
                input -= que[i];
                check = true;
            }
            else if(check)
                cout << "0";
        }
        cout << " (fib)" << endl;
    }

    return 0;
}
