#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int Hd, Ad, Hk, Ak, B, D;

int solve(int hd, int ad, int hk, int ak, int b, int d) {
	if (D == 0 && d > 0) return INT_MIN;
	if (B == 0 && b > 0) return INT_MIN;
	int turn = 0;
	int just_cured = 0;
	while (hk > 0 && hd > 0) {
		turn++;
		// Only cure if next hit is fatal and I don't kill first
		int need_cure = 1;
		if (ad >= hk) need_cure = 0;
		if (hd > ak)  need_cure = 0;
		if (d > 0 && hd > MAX(0, ak - D)) need_cure = 0;
		if (need_cure) {
			if (just_cured)
				return INT_MIN;
			hd = Hd;
			just_cured = 1;
		} else if (d > 0) {
			// First try to lower enemy's attack
			d--;
			ak = MAX(0, ak - D);
			just_cured = 0;
		} else if (b > 0) {
			// Then increase own attack
			b--;
			ad += B;
			just_cured = 0;
		} else {
			// We are setup, just strike
			hk -= ad;
			just_cured = 0;
		}
		// Knight's attack
		if (hk > 0)
			hd -= ak;
	}
	return hd > 0 ? turn : INT_MIN;
}

int main() {
	int t, x = 1;
	scanf("%d\n", &t);
	while (t--) {
		scanf("%d %d %d %d %d %d\n", &Hd, &Ad, &Hk, &Ak, &B, &D);
		int best = INT_MIN;
		for (int d = 0; d <= 100; ++d) {
			for (int b = 0; b <= 100; ++b) {
				int r = solve(Hd, Ad, Hk, Ak, b, d);
				if (best < 0 || (r > 0 && r < best))
					best = r;
			}
		}
		printf("Case #%d: ", x++);
		if (best < 0) printf("IMPOSSIBLE\n");
		else          printf("%d\n", best);
	}
	return 0;
}
