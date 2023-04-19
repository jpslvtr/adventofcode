#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "../utils/utils.h"

int p2(char *input) {
    int floor = 0;
    int position = 0;
    // Return the first time Santa's position is in the
    // basement, or -1.
    for(int i = 0; i < strlen(input); i++) {
        position += 1;
        if(input[i] == '(') {
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
    char *input = read_chars("in.txt");
    int res = p2(input);
    printf("res: %d\n", res);
    return 0;
}