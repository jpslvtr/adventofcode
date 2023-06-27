// Function declarations and definitions

char *read_chars(char *filename) {
    FILE *fp = fopen(filename, "r");
    fseek(fp, 0, SEEK_END);
    long fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    char *str = malloc(fsize + 1);
    fread(str, fsize, 1, fp);
    fclose(fp);

    return str;
}

