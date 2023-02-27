#include <stdlib.h>
#include <stdio.h>

int test(FILE* fp) {
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    while((read = getline(&line, &len, fp)) != -1) {

    }
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = test(fp);
    fclose(fp);
    printf("test: %d\n", res);
    return 0;
}
