#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define TIMES 5

void *proc()
{
	int a = 0;
	while (a < 2000) {
		printf("%d ", a);
		a++;
	}
}

int main() {

	pthread_t *tid = malloc(TIMES * sizeof(pthread_t));
	
	for (int i = 0; i < TIMES; i++) {
		pthread_create(&tid[i], NULL, proc, NULL);
		printf("A");
	}
		
	for (int i = 0; i < TIMES; i++)
		pthread_join(tid[i], NULL);

	return 0;
}
