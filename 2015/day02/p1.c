#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int wrappingPaper(FILE *fp) {
    int total = 0;
    char *line = NULL;
    size_t len = 0; // base unsigned int returned by sizeof()
                    // stores the max size of any type
    ssize_t read;   // same as size_t, but could also return negative error val
    while((read = getline(&line, &len, fp)) != -1) {
        int l = atoi(strtok(line, "x"));
        int w = atoi(strtok(NULL, "x"));
        int h = atoi(strtok(NULL, "x"));
        int smallest;
        if(l*w <= w*h && l*w <= h*l) {
            smallest = l*w;
        }
        else if(w*h <= l*w && w*h <= h*l) {
            smallest = w*h;
        }
        else {
            smallest = h*l;
        }
        int paper = (2*l*w) + (2*w*h) + (2*h*l) + smallest;
        total += paper;
    }
    return total;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = wrappingPaper(fp);
    fclose(fp);
    printf("total paper: %d\n", res);
    return 0;
}
