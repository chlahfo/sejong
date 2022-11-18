//유클리드 호제법 이용 - 최대공약수 구하기.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int gcd(int x, int y);

int main(void) {
	int a, b;
	printf("최대 공약수를 구할 두 수를 입력해주세요: \n");
	scanf("%d %d", &a, &b);
	printf("%d\n", gcd(a, b));
	if (gcd(a, b) == 1)
		printf("두 수는 서로소 입니다.");
	return 0;
}

//x는 y보다 커야 한다.
int gcd(int x, int y) {
	if (y == 0)
		return x;
	else
		return gcd(y, x % y);//순환호출
} 