CXX = g++
CXXFLAGS = -Wall -Wextra -O2 -std=c++17
d ?= 01

# Usage: make run d=01

run:
	mkdir -p ../bin
	$(CXX) $(CXXFLAGS) $(d).cpp utils/read_lines.cpp -o ../bin/$(d)
	../bin/$(d)
