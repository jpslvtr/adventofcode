#include "read_lines.h"
#include <fstream>

using namespace std;

vector<string> read_lines(string& filename) {
    ifstream fs(filename);
    vector<string> lines;
    string line;

    while (getline(fs, line)) {
        lines.push_back(line);
    }

    return lines;
}