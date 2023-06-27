#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int containsThreeVowels(char *s) {
    int count = 0;
    for(int i=0; i<strlen(s); i++) {
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || 
           s[i] == 'o' || s[i] == 'u') {
            count++;
        }
    }
    return (count >= 3);
}

int containsPairDuplicate(char *s) {
    char *str = s + 1;
    char prev = *s;
    for(int i=0; i<strlen(str); i++) {
        if(str[i] == prev) {
            return 1;
        }
        prev = str[i];
    }
    return 0;
}

int includesSubstring(char *s) {
    return (strstr(s, "ab") || strstr(s, "cd") ||
            strstr(s, "pq") || strstr(s, "xy"));
}

int niceCount(FILE *fp) {
    int nice = 0;
    char *s = NULL;
    size_t len = 0;
    ssize_t read;
    while((read = getline(&s, &len, fp)) != -1) {
        if(containsThreeVowels(s) && containsPairDuplicate(s) && 
           !includesSubstring(s)){
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
