#include <stdio.h>
#define ROWS 3
#define COLS 5

int main(void) {
	int a[ROWS][COLS] = { 
		{86, 98, 80, 76, 3}, 
		{99, 89, 90, 90, 0}, 
		{65, 68, 50, 49, 0} 
	};

	int i;

	for (i = 0; i < ROWS;i++) {
		double final_scores = a[i][0] * 0.3 + a[i][1] * 0.4 + a[i][2] * 0.2 + a[i][3] * 0.1 - a[i][4];
		//중간고사 30% + 기말고사 40% + 기말과제 0.2 + 과제 0.3 - 감점
		printf("학생 #%d의 최종성적 = %10.2f\n", i + 1, final_scores);//전체자리수 10자리에서 2자리까지 나타낸다는 뜻.
	}
	return 0;
}