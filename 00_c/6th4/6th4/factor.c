#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long factorial(int n) {
	long result = 1;
	//곱하기때문에 초기값은 0이면 안됨
	for (int i = 1; i <= n; i++)
	result *= i;
		
	return result;
}

int main(void) {
	int n;
	printf("알고 싶은 팩토리얼의 값은?");
	scanf("%d", &n);
	printf("%d!의 값은 %d입니다. \n", n, factorial(n));

	return 0;
}