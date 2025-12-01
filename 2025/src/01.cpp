#include <iostream>
#include <vector>
#include <string>
#include "utils/read_lines.h"

using namespace std;

int part1(string& filename) {
    vector<string> lines = read_lines(filename);

    int position = 50; // starting dial position
    int dial_size = 100; // 0-99 positions on dial
    int zero_count = 0; // how many times dial lands on zero

    for (size_t i = 0; i < lines.size(); i++) {
        const string& line = lines[i];

        char dir = line[0]; // L or R
        int dist = stoi(line.substr(1)); // remaining chars = dist

        // convert distance to equivalent movement in the dial's range
        int move = dist % dial_size;

        if (dir == 'L') {
            position -= move;
            if (position < 0) {
                position += dial_size; // wrap if position is negative
            }
        }
        else if (dir == 'R') {
            position += move;
            if (position >= dial_size) {
                position -= dial_size; // wrap if position exceeds max
            }
        }

        if (position == 0) {
            zero_count++;
        }
    }

    return zero_count;
}

int part2(string& filename) {
    vector<string> lines = read_lines(filename);
    return 0;
}

int main() {
    string input_file = "../input/01.txt";
    cout << part1(input_file) << "\n";
    cout << part2(input_file) << "\n";
    return 0;
}