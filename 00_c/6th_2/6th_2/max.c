//두 수 중에서 큰 수를 찾는 함수 예제
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int get_max(int x, int y) {
	if (x > y) return (x);
	else return (y);
}

int main() {
	int a, b;

	printf("두개의 정수를 입력하시오:");
	scanf("%d %d", &a, &b);

	printf("두 수 중에서 가장 큰 변수는 %d 입니다 \n", get_max(a, b));//함수 호출
	
	return 0;
}