#include <stdio.h>

char flag[31] = {58, 43, 43, 56, 46, 51, 44, 34, 56, 30, 42, 73, 14, 42, 50, 56, 67, 16, 39, 72, 30, 62, 56, 18, 64, 35, 13, 53, 1, 28, 0};
int affichage = 0;


void decript(char *key) {

	int i = -1;
	int y = 0;

	while (flag[++i] != 0) {
		if (affichage)
			printf("%c", flag[i]^key[y]);
		if (key[++y] == 0)
			y = 0;
	}

}

int main(int argc, char **argv) {
	
	if (argc < 3)
		return 0;
	
	if (argv[2][0] == '1' && argv[2][1] == 0)
		affichage = 1;
	decript(argv[1]);
	
	return 0;
}
