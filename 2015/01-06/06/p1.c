#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define width 1000
#define height 1000

void toggle(int grid[width][height], int from[], int to[]) {
    for(int x=from[0]; x<=to[0]; x++) {
        for(int y = from[1]; y<=to[1]; y++) {
            grid[x][y] = !grid[x][y];
        }
    }
}

void turnOn(int grid[width][height], int from[], int to[]) {
    for(int x=from[0]; x<=to[0]; x++) {
        for(int y = from[1]; y <=to[1]; y++) {
            grid[x][y] = 1;
        }
    }
}

void turnOff(int grid[width][height], int from[], int to[]) {
    for(int x=from[0]; x<=to[0]; x++) {
        for(int y = from[1]; y <=to[1]; y++) {
            grid[x][y] = 0;
        }
    }
}

int litLights(FILE* fp) {
    char *s = NULL;
    size_t len = 0;
    ssize_t read;
    int grid[width][height] = {0};
    int from[2] = {0,0};
    int to[2] = {0,0};
    int count = 0;
    while((read = getline(&s, &len, fp)) != -1) {
        if(sscanf(s, "toggle %d,%d through %d,%d\n", &from[0], &from[1], &to[0], &to[1])) {
            toggle(grid, from, to);
        } else if(sscanf(s, "turn on %d,%d through %d,%d\n", &from[0], &from[1], &to[0], &to[1])) {
            turnOn(grid, from, to);
        } else if(sscanf(s, "turn off %d,%d through %d,%d\n", &from[0], &from[1], &to[0], &to[1])) {
            turnOff(grid, from, to);
        }
    }
    for(int x=0; x<width; x++) {
        for(int y=0; y<height; y++) {
            count += grid[x][y];
        }
    }
    return count;
}

int main(void) {
    FILE *fp = fopen("in.txt", "r");
    int res = litLights(fp);
    fclose(fp);
    printf("res: %d\n", res);
    return 0;
}
