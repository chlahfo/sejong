#include <stdio.h>

//amount �� ����̸� �Ա��̰�, �����̸� ������� �����Ѵ�. 
void save(int amount) {
	static long balance = 0;//�ܰ�(�ʱⰪ. �ѹ��� �ʱ�ȭ �ǹǷ� static�� ���� ��)

	if (amount >= 0)
		printf("%d\t\t", amount);//�Ա�
	else
		printf("\t%d\t", -amount);//���

	balance += amount;//���� balance = balance + amount
	printf("%d \n", balance);
}

int main() {
	printf("=========================================\n");
	printf("�Ա�\t ���\t �ܰ�\n");
	printf("=========================================\n");
	save(10000);
	save(50000);
	save(-10000);
	save(30000);
	printf("=========================================\n");
	//printf("%d", balance); ���������̹Ƿ� �ȵ����� ���� �ð��� ����ð� ���� �Բ���.
	return 0;
}