//�л� 5���� ������ �Է¹޾� ����� ���ϴ� ���α׷�
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define STUDENTS 10//��ȣ���

int main(void) {
	int scores[STUDENTS];
	int sum = 0;
	int i, average;

	for (i = 0; i < STUDENTS; i++) {
		printf("�л����� ������ �Է��Ͻÿ�: ");
		scanf("%d", &scores[i]);
	}
	for (i = 0; i < STUDENTS; i++)
		sum += scores[i];

	//�� for ���� ���� ��������
	
	average = sum / STUDENTS;
	printf("���� ��� = %d\n", average);

	return 0;
}