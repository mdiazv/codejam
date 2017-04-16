#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int qtty;
	int minK;
	int maxK;
} pack_t;

int N, P;
int R[64];
int I[64];
pack_t Q[64][64];

int packcmp(const void *a, const void *b) {
	const pack_t *aa = a;
	const pack_t *bb = b;
	
	if (aa->minK == bb->minK)
		return aa->maxK - bb->maxK;
	return aa->minK - bb->minK;
}

int intersect(int i, int j, int *m, int *M) {
	if (*m < Q[i][j].minK) *m = Q[i][j].minK;
	if (Q[i][j].maxK < *M) *M = Q[i][j].maxK;
	return *m <= *M;
}

int done() {
	for (int i = 0; i < N; ++i)
		if (I[i] == P)
			return 1;
	return 0;
}

int solve() {
	int r = 0;
	memset(I, 0, sizeof(I));
	for (int i = 0; i < N; ++i)
		while (I[i] < P && Q[i][I[i]].maxK == 0)
			I[i]++;
	while (!done()) {
		int ok = 1, m = 0, M = 10000000;
		for (int i = 0; i < N; ++i) {
			if (!intersect(i, I[i], &m, &M)) {
				ok = 0;
				int worst = 0;
				for (int j = 1; j < N; ++j)
					if (Q[j][I[j]].maxK < Q[worst][I[worst]].maxK)
						worst = j;
				I[worst]++;
				break;
			}
		}
		if (ok) {
			r++;
			for (int i = 0; i < N; ++i)
				I[i]++;
		}
	}
	return r;
}

int main() {
	int t, x = 1;
	scanf("%d\n", &t);
	while (t--) {
		scanf("%d %d\n", &N, &P);
		for (int i = 0; i < N; ++i)
			scanf("%d ", &R[i]);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				scanf("%d ", &Q[i][j].qtty);
				Q[i][j].minK = 0;
				Q[i][j].maxK = 0;
				int inf = (Q[i][j].qtty * 100) / (R[i] * 110);
				int sup = (Q[i][j].qtty * 100) / (R[i] *  90);
				for (int k = inf; k <= sup; ++k) {
					if (R[i] * k * 90 <= Q[i][j].qtty * 100 && R[i]  * k * 110 >= Q[i][j].qtty * 100) {
						Q[i][j].minK = k;
						break;
					}
				}
				for (int k = sup; k >= inf; --k) {
					if (R[i]  * k * 90 <= Q[i][j].qtty * 100 && R[i]  * k * 110 >= Q[i][j].qtty * 100) {
						Q[i][j].maxK = k;
						break;
					}
				}
			}
			qsort(Q[i], P, sizeof(pack_t), packcmp);
		}
		printf("Case #%d: %d\n", x++, solve());
	}
	return 0;
}
