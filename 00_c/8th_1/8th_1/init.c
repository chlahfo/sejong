#include <stdio.h>

//�Լ� ����
void init();

int main(void) {
	//�ѹ��� �ʱ�ȭ�ϱ�

	init();
	init();
	init();
	return 0;
}

void init(void) {
	static int inited = 0;//��������. �ѹ��� �ʱ�ȭ�Ǵ� Ư¡�� ����.

	if (inited == 0) {
		printf("init(): ��Ʈ��ũ ��ġ�� �ʱ�ȭ�մϴ�. \n");
		inited = 1;
	}
	else {
		printf("init(): �̹� �ʱ�ȭ�Ǿ����Ƿ� �ʱ�ȭ���� �ʽ��ϴ�. \n");
	}
}