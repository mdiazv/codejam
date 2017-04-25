#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define debug(...) fprintf(stderr, __VA_ARGS__)

int N;
int count[6];
char *color = "ROYGBV";
char R[1024];
char S[1024];
int len[3];
char s[3][1024];

int maxcount() {
	int max = -1, maxp = -1;
	for (int i = 0; i < 6; ++i)
		if (count[i] && count[i] > max)
			max = count[i], maxp = i;
	return maxp;
}

int indexof(char c) {
	char *p = strchr(color, c);
	return p - color;
}

int small(int N) {
	memset(S, 0, sizeof(S));
	if (N == 0)
		return 0;
	if (N == 1)
		return -1;
	int k = maxcount();
	for (int i = 0; i < 6; i += 2)
		if (count[k] > N/2)
			return -1;
	int i;
	while (k != -1) {
		for (; i < N && count[k]; i += 2) {
			S[i] = color[k];
			count[k]--;
		}
		if (i >= N)
			i = 1;
		if (count[k] == 0)
			k = maxcount();
	}
	debug("prim -> %s\n", S);
	return 0;
}

int solve() {
	memset(len, 0, sizeof(len));
	memset(s, 0, sizeof(s));
	memset(R, 0, sizeof(R));
	for (int i = 0; i < 6; ++i)	
		debug("%d ", count[i]);
	debug("\n");
	int even, evenp;
	for (int i = 0; i < 3; ++i) {
		int sec = 2*i+1;
		int prim = (2*i+1+3)%6;
		if (count[sec]) {
			if (count[prim] < count[sec])
				return -1;
			for (int j = 0; j < count[sec]; ++j) {
				s[i][2*j] = color[prim];
				s[i][2*j+1] = color[sec];
			}
			len[i] = 2*count[sec];
			if (count[prim] > count[sec]) {
				s[i][2*count[sec]] = color[prim];
				len[i]++;
				count[prim]--;
			}
			if (len[i] > 0) {
				count[prim]++;
				if (len[i] % 2 == 0)
					even++, evenp = i;
			}
			count[prim] -= count[sec];
			count[sec] = 0;
		}
	}
	int sum = 0;
	for (int i = 0; i < 6; ++i)	
		sum += count[i];
	for (int i = 0; i < 3; ++i) {
		debug("%c (%d) -> %s\n", color[2*i+1], len[i], s[i]);
	}
	for (int i = 0; i < 6; ++i)	
		debug("%d ", count[i]);
	debug("(%d)\n", sum);
	if (even) {
		if (sum > 1)
			return -1;
		memcpy(R, s[evenp], len[evenp]);
		return 0;
	}

	if (small(sum) < 0)
		return -1;

	int off = 0;
	for (int i = 0; i < sum; ++i) {
		int j = (indexof(S[i]) / 2 + 1) % 3;
		if (len[j]) {
			debug("Replacing first %c (at %d) for %s\n", S[i], i, s[j]);
			memcpy(R + off, s[j], len[j]);
			off += len[j];
			len[j] = 0;
		} else {
			R[off++] = S[i];
		}
	}

	return 0;
}

int main() {
	int t, x = 1;
	scanf("%d\n", &t);
	while (t--) {
		scanf("%d ", &N);
		for (int i = 0; i < 6; ++i)	
			scanf("%d ", &count[i]);
		if (solve() < 0)
			printf("Case #%d: IMPOSSIBLE\n", x++);
		else
			printf("Case #%d: %s\n", x++, R);
	}
	return 0;
}
