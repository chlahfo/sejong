#include <stdio.h>

//amount 가 양수이면 입금이고, 음수이면 출금으로 생각한다. 
void save(int amount) {
	static long balance = 0;//잔고(초기값. 한번만 초기화 되므로 static을 써준 것)

	if (amount >= 0)
		printf("%d\t\t", amount);//입금
	else
		printf("\t%d\t", -amount);//출금

	balance += amount;//누적 balance = balance + amount
	printf("%d \n", balance);
}

int main() {
	printf("=========================================\n");
	printf("입금\t 출금\t 잔고\n");
	printf("=========================================\n");
	save(10000);
	save(50000);
	save(-10000);
	save(30000);
	printf("=========================================\n");
	//printf("%d", balance); 지역변수이므로 안되지만 생존 시간은 실행시간 내내 함께함.
	return 0;
}