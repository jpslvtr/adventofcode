#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "../utils/utils.h"

int p1(char *input) {
    int floor = 0;
    // If character is (, go up one floor. If character is ), 
    // go down one floor. Return floor.
    for(int i = 0; i < strlen(input); i++) {
        if(input[i]== '(') {
            floor += 1;
        } 
        else {
            floor -= 1;
        }
    }
    return floor;
}

int main(void) {
    char *input = read_chars("in.txt");
    int res = p1(input);
    printf("res: %d\n", res);
    return 0;
}