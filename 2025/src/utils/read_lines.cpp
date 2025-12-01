#include "read_lines.h"
#include <fstream>

using namespace std;

vector<string> read_lines(const string& filename) {
    ifstream file(filename);
    vector<string> lines;
    string line;

    while (getline(file, line)) {
        if (!line.empty() && line.back() == '\r') {
            line.pop_back();
        }
        lines.push_back(line);
    }

    return lines;
}
