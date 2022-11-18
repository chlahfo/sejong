//배열을 이용하여 간단한 극장 예약 시스템을 작성. 단, 좌석은 10개, 예약 완료 좟거은 1, 예약이 안된 좌석은 0으로 나타남
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define SIZE 10

//기호상수

int main(void) {
	char ans1;
	int ans2, i;
	int seats[SIZE] = { 0 };

	while (1) {
		printf("좌석을 예약하시겠습니까?(y 또는 n)\n");
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
			printf("몇번째 좌석을 예약하시겠습니까?");
		}
		scanf("%d", &ans2);
		if (ans2 <= 0 || ans2 > SIZE) {
			printf("1부터 10사이의 숫자를 입력하세요. \n");
			continue;
		}
		if (seats[ans2 - 1] == 0) {
			seats[ans2 - 1] = 1;
			printf("예약되었습니다. \n");
		} else {
			printf("이미 예약된 자리입니다. \n");
		}
	}
	
	return 0;
}