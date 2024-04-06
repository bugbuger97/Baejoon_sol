#include <iostream> 
using namespace std;

int main() {
	int num;
	cin >> num;
	for (int i = 1; i <= num; i++) { // for(초기화; 반복 조건; 증감식)
		for (int j = 0; j < i; j++) {
			cout << '*';
		}
		cout << endl;
	}
	return 0;
}