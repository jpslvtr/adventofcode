#include <stdlib.h>
#include <stdio.h>

int firstEnterBasement(FILE* fp) {
    int floor = 0;
    int position = 0;
    char c;
    while((c = fgetc(fp)) != EOF) {
        position += 1;
        if(c == '(') {
            floor += 1;
        } 
        else {
            floor -= 1;
        }
        if(floor == -1) {
            break;
        }
    }
    return position;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = firstEnterBasement(fp);
    fclose(fp);
    printf("res: %d\n", res);
    return 0;
}