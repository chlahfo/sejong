//�� �� �߿��� ū ���� ã�� �Լ� ����
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int get_max(int x, int y) {
	if (x > y) return (x);
	else return (y);
}

int main() {
	int a, b;

	printf("�ΰ��� ������ �Է��Ͻÿ�:");
	scanf("%d %d", &a, &b);

	printf("�� �� �߿��� ���� ū ������ %d �Դϴ� \n", get_max(a, b));//�Լ� ȣ��
	
	return 0;
}