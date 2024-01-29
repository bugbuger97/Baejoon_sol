#include <iostream>
using namespace std;

int main(){
    int i;
    int result = 1;
    cin >> i;
    for (i; i > 1; i--){
        result *= i;
    }
    cout << result;
    return 0;
}