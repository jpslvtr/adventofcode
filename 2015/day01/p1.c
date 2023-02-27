#include <stdlib.h>
#include <stdio.h>

int santasFloor(FILE* fp) {
    int floor = 0;
    char c;
    while((c = fgetc(fp)) != EOF) {
        if(c == '(') {
            floor += 1;
        } 
        else {
            floor -= 1;
        }
    }
    return floor;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = santasFloor(fp);
    fclose(fp);
    printf("res: %d\n", res);
    return 0;
}
