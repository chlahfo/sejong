//�迭�� �̿��Ͽ� ������ ���� ���� �ý����� �ۼ�. ��, �¼��� 10��, ���� �Ϸ� �ư��� 1, ������ �ȵ� �¼��� 0���� ��Ÿ��
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define SIZE 10

//��ȣ���

int main(void) {
	char ans1;
	int ans2, i;
	int seats[SIZE] = { 0 };

	while (1) {
		printf("�¼��� �����Ͻðڽ��ϱ�?(y �Ǵ� n)\n");
		scanf("%c", &ans1);

		if (ans1 == 'y') {
			printf("-----------------------------------\n");
			for (int j = 0; j < SIZE; j++) {
				printf("%d\t", j + 1);
			}
			printf("\n-----------------------------------\n");
			for (i = 0; i < SIZE; i++) {
				printf("%d\t", seats[i]);
			}
			printf("\n");
			printf("���° �¼��� �����Ͻðڽ��ϱ�?");
		}
		scanf("%d", &ans2);
		if (ans2 <= 0 || ans2 > SIZE) {
			printf("1���� 10������ ���ڸ� �Է��ϼ���. \n");
			continue;
		}
		if (seats[ans2 - 1] == 0) {
			seats[ans2 - 1] = 1;
			printf("����Ǿ����ϴ�. \n");
		} else {
			printf("�̹� ����� �ڸ��Դϴ�. \n");
		}
	}
	
	return 0;
}