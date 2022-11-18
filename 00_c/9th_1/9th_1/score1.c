//학생 5명의 성적을 입력받아 평균을 구하는 프로그램
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define STUDENTS 10//기호상수

int main(void) {
	int scores[STUDENTS];
	int sum = 0;
	int i, average;

	for (i = 0; i < STUDENTS; i++) {
		printf("학생들의 성적을 입력하시오: ");
		scanf("%d", &scores[i]);
	}
	for (i = 0; i < STUDENTS; i++)
		sum += scores[i];

	//왜 for 문을 따로 나눴을까
	
	average = sum / STUDENTS;
	printf("성적 평균 = %d\n", average);

	return 0;
}