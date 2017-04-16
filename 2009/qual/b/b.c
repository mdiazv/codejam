#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int H, W;
int map[128][128];
char sol[128][128];
char nextsink;

int get(int i, int j) {
	if (i < 0 || i >= H || j < 0 || j >= W)
		return INT_MAX;
	return map[i][j];
}

char flood(int i, int j) {
	if (sol[i][j] != '.')
		return sol[i][j];

	int nbs[4] = {get(i-1, j), get(i, j-1), get(i, j+1), get(i+1, j)};
	int move[4][2] = {{i-1, j}, {i, j-1}, {i, j+1}, {i+1, j}};
	int min = nbs[0];
	for (int k = 1; k < 4; ++k)
		if (nbs[k] < min)
			min = nbs[k];

	if (min >= get(i, j)) {
		sol[i][j] = nextsink++;
		return sol[i][j];
	}

	for (int k = 0; k < 4; ++k) {
		if (nbs[k] == min) {
			sol[i][j] = flood(move[k][0], move[k][1]);
			break;
		}
	}
	
	return sol[i][j];
}

void solve() {
	nextsink = 'a';
	for (int i = 0; i < H; ++i)
		for (int j = 0; j < W; ++j)
			flood(i, j);
}

int main() {
	int t, x = 1;
	scanf("%d\n", &t);
	while (t--) {
		scanf("%d %d\n", &H, &W);
		for (int i = 0; i < H; ++i)
			for (int j = 0; j < W; ++j)
				scanf("%d ", &map[i][j]);
		memset(sol, '.', sizeof(sol));
		solve();
		printf("Case #%d:\n", x++);
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j)
				printf("%s%c", j ? " " : "", sol[i][j]);
			printf("\n");
		}
	}
	return 0;
}
