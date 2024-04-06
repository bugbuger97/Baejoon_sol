#include <iostream>
using namespace std;

int main() {
	int N;
	int score[1000];
	int max = -1;
	float total = 0;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> score[i];
		if (score[i] > max) {
			max = score[i];
		}
		total += score[i];
	}
	cout << total *100 / (max * N);
	return 0;
}