#include <stdlib.h>
#include <stdio.h>

int test(FILE* fp) {
    return 0;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = test(fp);
    fclose(fp);
    printf("test: %d\n", res);
    return 0;
}