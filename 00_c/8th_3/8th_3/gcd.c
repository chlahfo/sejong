//��Ŭ���� ȣ���� �̿� - �ִ����� ���ϱ�.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int gcd(int x, int y);

int main(void) {
	int a, b;
	printf("�ִ� ������� ���� �� ���� �Է����ּ���: \n");
	scanf("%d %d", &a, &b);
	printf("%d\n", gcd(a, b));
	if (gcd(a, b) == 1)
		printf("�� ���� ���μ� �Դϴ�.");
	return 0;
}

//x�� y���� Ŀ�� �Ѵ�.
int gcd(int x, int y) {
	if (y == 0)
		return x;
	else
		return gcd(y, x % y);//��ȯȣ��
} 