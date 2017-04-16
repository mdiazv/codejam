#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;
int DP[512][32];
char S[512];
char *W = "welcome to code jam";

int welcome(int i, int j) {
	if (j == 19) return 1;
	if (i ==  N) return 0;
	if (DP[i][j] >= 0)
		return DP[i][j];

	int r = 0;
	if (S[i] == W[j])
		r += welcome(i+1, j+1) % 10000;
	r += welcome(i+1, j) % 10000;

	return DP[i][j] = r % 10000;
}

int main() {
	int t, x = 1;
	scanf("%d\n", &t);
	while (t--) {
		scanf("%[^\n]%n\n", S, &N);
		memset(DP, -1, sizeof(DP));
		int w = welcome(0, 0);
		printf("Case #%d: %.4d\n", x++, w);
	}
	return 0;
}
