#include <iostream>
using namespace std;

int main() {
	int a[9];
	int Max_value = -1;
	int index = 0;
	for (int i = 0; i < 9; i++) {
		cin >> a[i];
		if (a[i] > Max_value) {
			Max_value = a[i];
			index = i;
		}
	}
	cout << Max_value << endl << index + 1;
	return 0;
}