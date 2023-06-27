#include <stdlib.h>
#include <stdio.h>

typedef struct House {
    int x;
    int y;
    struct House *next;
} House;

int addHouse(int x, int y, House *unit) {
	while((*unit).x != x || (*unit).y != y) {
		if((*unit).next != NULL) {
			unit = (*unit).next;
		} else {
            (*unit).next = (House *)malloc(sizeof(House));
            (*(*unit).next).x = x;
            (*(*unit).next).y = y;
            (*(*unit).next).next = NULL;
			return 1;
		}
	}
	return 0;
}

void freeHouses(House *unit) {
    House *curr;
    House *prev;
    curr = prev = unit;
	while((*curr).next) {
		prev = curr;
		curr = (*curr).next;
		free(prev);
	}
}

int countHouses(FILE* fp) {
    // ptr that stores the address of curr on the heap
    House *curr;
    // dynamic allocation
    curr = (House *)malloc(sizeof(House));
    // derefernces ptr and gives us access to what curr is pointing to
    (*curr).x = 0;
    (*curr).y = 0;
    (*curr).next = NULL;
    int x[2] = {0};
    int y[2] = {0};
    int houses = 1; // first house
    int deliverer = 0;
    char c;
    while((c = fgetc(fp)) != EOF) {
        switch(c) {
            case '^':
                y[deliverer]++;
                break;
            case 'v':
                y[deliverer]--;
                break;
            case '>':
                x[deliverer]++;
                break;
            case '<':
                x[deliverer]--;
                break;
        }
        houses += addHouse(x[deliverer], y[deliverer], curr);
        deliverer = !deliverer;
    }
    freeHouses(curr);
    return houses;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = countHouses(fp);
    fclose(fp);
    printf("res: %d\n", res);
    return 0;
}
