#include <iostream>
#include <string>
using namespace std;

int main(){
    string a;
    int temp1; // 1의 자리
    int temp2; // 10의 자리
    int cnt = 0; // 사이클
    cin >> a;
    string result = a;
    for (int i=0; i<100; i++){
        temp1 = atoi(result.c_str()) % 10;
        temp2 = atoi(result.c_str()) / 10;  
        if (temp1 + temp2 < 10){
            if (result[1] == 0){
                result = result[0] + to_string(temp1+temp2);
            }
            else{
                result = result[1] + to_string(temp1+temp2);
            }
        }
        else{
            if (result[1] == 0){
                result = result[0] + to_string((temp1 + temp2) % 10);
            }
            else{
                result = result[1] + to_string((temp1 + temp2) % 10);
            }
        }
        if (atoi(result.c_str()) == atoi(a.c_str())){
            cout << i+1;
            break;
        }
    }
     return 0;
}