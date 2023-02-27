#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int containsPair(char *s) {
    char *str = s + 2;
    char *prev = s;
    while(*str) {
        if (*str == *prev) {
            return 1;
        }
        prev++;
        str++;
    }

    return 0;
}

int containsAdjacentRepeats(char *s) {
    char pair[3];
    while(*s) {
        strncpy(pair, s, sizeof(pair)-1);
        if (strstr(s + 2, pair))
            return 1;
        s++;
    }
    return 0;
}

int niceCount(FILE *fp) {
    int nice = 0;
    char *s = NULL;
    size_t len = 0;
    ssize_t read;
    while((read = getline(&s, &len, fp)) != -1) {
        if(containsPair(s) && containsAdjacentRepeats(s)){
            nice++;
        }
    }
    return nice;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = niceCount(fp);
    fclose(fp);
    printf("res: %d\n", res);
    return 0;
}
