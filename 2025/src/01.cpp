#include <iostream>
#include <vector>
#include <string>
#include "utils/read_lines.h"

using namespace std;

int part1(const string& filename) {
    vector<string> lines = read_lines(filename);

    int position = 50;
    int zero_count = 0;
    const int dial_size = 100;

    for (int i = 0; i < lines.size(); i++) {
        char dir;
        int dist;

        if (sscanf(lines[i].c_str(), "%c%d", &dir, &dist) != 2) {
            continue;
        }

        int move = dist % dial_size;

        if (dir == 'L') {
            position -= move;
            if (position < 0) position += dial_size;
        }
        else if (dir == 'R') {
            position += move;
            if (position >= dial_size) position -= dial_size;
        }

        if (position == 0) zero_count++;
    }

    return zero_count;
}

int main() {
    string input_file = "../input/01.txt";
    cout << part1(input_file) << "\n";
    return 0;
}