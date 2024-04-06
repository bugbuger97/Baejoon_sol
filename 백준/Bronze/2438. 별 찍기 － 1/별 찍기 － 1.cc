#include <iostream> 
#include <string>
using namespace std;

int main() {
	string star = "";
	int num;
	cin >> num;
	for (int i = 1; i <= num; i++) { 
		star += "*";
		cout << star << endl;
	}
	return 0;
}