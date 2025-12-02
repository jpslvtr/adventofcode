#include <iostream>
#include <vector>
#include <string>
#include "utils/read_lines.h"
using namespace std;

// CONSTANTS
constexpr int START_POS = 50;
constexpr int DIAL_SIZE = 100;

// PART 1
int part1(vector<string>& lines) {
    int position = START_POS; // starting dial position
    int zero_count = 0; // how many times dial lands on zero

    for (size_t i = 0; i < lines.size(); i++) {
        string& line = lines[i];

        char dir = line[0]; // L or R
        int dist = stoi(line.substr(1)); // remaining chars = dist

        // convert distance to equivalent movement in the dial's range
        int move = dist % DIAL_SIZE;

        if (dir == 'L') {
            position -= move;
            if (position < 0) {
                position += DIAL_SIZE; // wrap if position is negative
            }
        } else if (dir == 'R') {
            position += move;
            if (position >= DIAL_SIZE) {
                position -= DIAL_SIZE; // wrap if position exceeds max
            }
        }

        if (position == 0) {
            zero_count++;
        }
    }

    return zero_count;
}

// PART 2
int part2(vector<string>& lines) {
    int position = START_POS; // starting dial position
    int zero_count = 0; // how many times dial lands on zero

    for (size_t i = 0; i < lines.size(); i++) {
        string& line = lines[i];

        char dir = line[0]; // L or R
        int dist = stoi(line.substr(1)); // remaining chars = dist

        int zeros_this_move = 0;

        if (dir == 'L') { // how many times do we pass 0 when moving left?
            if (position == 0) {
                zeros_this_move = dist / DIAL_SIZE;
            } else if (dist < position) {
                zeros_this_move = 0;
            } else {
                zeros_this_move = (dist - position) / DIAL_SIZE + 1;
            }
            int move = dist % DIAL_SIZE;
            position = (position - move + DIAL_SIZE) % DIAL_SIZE;
        }
        else if (dir == 'R') { // how many times do we pass 0 when moving left?
            zeros_this_move = (position + dist) / DIAL_SIZE;
            int move = dist % DIAL_SIZE;
            position = (position + move) % DIAL_SIZE;
        }
        zero_count += zeros_this_move;
    }

    return zero_count;
}

int main() {
    string input_file = "../input/01.txt";
    vector<string> lines = read_lines(input_file);
    cout << part1(lines) << "\n";
    cout << part2(lines) << "\n";
    return 0;
}