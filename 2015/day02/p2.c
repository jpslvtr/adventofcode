#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int totalRibbon(FILE *fp) {
    int total = 0;
    char *line = NULL;
    size_t len = 0; // base unsigned int returned by sizeof()
                    // stores the max size of any type
    ssize_t read;   // same as size_t, but could also return negative error val
    while((read = getline(&line, &len, fp)) != -1) {
        int l = atoi(strtok(line, "x"));
        int w = atoi(strtok(NULL, "x"));
        int h = atoi(strtok(NULL, "x"));
        int perimeter1 = (2*l + 2*w);
        int perimeter2 = (2*w + 2*h);
        int perimeter3 = (2*h + 2*l);
        int volume = l*w*h;
        int smallest;
        if(perimeter1 <= perimeter2 && perimeter1 <= perimeter3) {
            smallest = perimeter1;
        }
        else if(perimeter2 <= perimeter1 && perimeter2 <= perimeter3) {
            smallest = perimeter2;
        }
        else {
            smallest = perimeter3;
        }
        total += smallest + volume;
    }
    return total;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = totalRibbon(fp);
    fclose(fp);
    printf("total ribbon: %d\n", res);
    return 0;
}