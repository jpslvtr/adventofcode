#include "utils.hpp"
#include <fstream>
#include <iostream>

using namespace std;

int main() {
  int floor = 0;
  int position = 0;
  ifstream infile("../input/01.txt");
  char c;
  while(infile.get(c)) {
    position += 1;
    if(c == '(') {
      floor += 1;
    } 
    else {
      floor -= 1;
    }
    if(floor == -1) {
      break;
    }
  }
  cout << "part1: " << floor << endl;
  cout << "part2: " << position << endl;
  return 0;
}