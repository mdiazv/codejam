#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int R, C;
char cake[32][32];
int solved[32][32];

int main() {
	int t, x = 1;
	scanf("%d\n", &t);
	while (t--) {
		memset(solved, 0, sizeof(solved));
		scanf("%d %d\n", &R, &C);
		for (int i = 0; i < R; ++i)
			scanf("%s\n", cake[i]);

		for (int i = 0; i < R; ++i) {
			int j = 0;
			char first = '\0';
			while (j < C && cake[i][j] == '?')
				++j;
			while (j < C) {
				char c = cake[i][j++];
				if (!first)
					first = c;
				while (j < C && cake[i][j] == '?')
					cake[i][j++] = c;
			}
			if (first)
				for (j = 0; j < C; ++j)
					if (cake[i][j] == '?')
						cake[i][j] = first;
		}

		for (int i = 1; i < R; ++i) {
			if (cake[i][0] == '?')
				memcpy(cake[i], cake[i-1], sizeof(cake[i]));
		}

		for (int i = R-2; i >= 0; --i) {
			if (cake[i][0] == '?')
				memcpy(cake[i], cake[i+1], sizeof(cake[i]));
		}

		printf("Case #%d:\n", x++);
		for (int i = 0; i < R; ++i)
			printf("%s\n", cake[i]);
	}
	return 0;
}
