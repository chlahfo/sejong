#include <stdio.h>

//함수 원형
void init();

int main(void) {
	//한번만 초기화하기

	init();
	init();
	init();
	return 0;
}

void init(void) {
	static int inited = 0;//정적변수. 한번만 초기화되는 특징이 있음.

	if (inited == 0) {
		printf("init(): 네트워크 장치를 초기화합니다. \n");
		inited = 1;
	}
	else {
		printf("init(): 이미 초기화되었으므로 초기화하지 않습니다. \n");
	}
}