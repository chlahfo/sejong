#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long factorial(int n) {
	long result = 1;
	//���ϱ⶧���� �ʱⰪ�� 0�̸� �ȵ�
	for (int i = 1; i <= n; i++)
	result *= i;
		
	return result;
}

int main(void) {
	int n;
	printf("�˰� ���� ���丮���� ����?");
	scanf("%d", &n);
	printf("%d!�� ���� %d�Դϴ�. \n", n, factorial(n));

	return 0;
}