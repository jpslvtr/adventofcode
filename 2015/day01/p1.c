#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    printf("floor: %d\n", res);
    return 0;
}
