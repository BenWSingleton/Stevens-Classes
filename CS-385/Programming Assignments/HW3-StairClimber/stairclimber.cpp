/*******************************************************************************
 * Name        : stairclimber.cpp
 * Author      : Benjamin Singleton
 * Date        : 10/02/20
 * Description : Lists the number of ways to climb n stairs.
 * Pledge      : I pledge my honor that I have abided by the Stevens Honor System.
 ******************************************************************************/
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>

using namespace std;

vector< vector<int> > get_ways(int num_stairs) {
    // TODO: Return a vector of vectors of ints representing
    // the different combinations of ways to climb num_stairs
    // stairs, moving up either 1, 2, or 3 stairs at a time.
	vector< vector<int> > combos;
	if (num_stairs <= 0) {
		combos.push_back(vector<int>());
	} else {
		for (int i = 1; i <= 3; i++) {
			if (num_stairs >= i) {
				vector< vector<int> > result = get_ways(num_stairs - i);
				for (unsigned int j = 0; j < result.size(); j++) {
					result[j].insert(result[j].begin(), i);
				}
				combos.insert(combos.end(), result.begin(), result.end());
			}
		}
	}
	return combos;
}

void display_ways(const vector< vector<int> > &ways) {
    // TODO: Display the ways to climb stairs by iterating over
    // the vector of vectors and printing each combination.
	int count = 0;
	int max = ways[0].size();
	int counter = 1;

	//cout << "num[0]: " << ways[0].size() << endl;
	//cout << "num: " << ways.size() << endl;
	if (ways.size() == 1) {
		cout << ways.size() << " way to climb " << ways[0].size() << " stair." << endl;
	} else {
		cout << ways.size() << " ways to climb " << ways[0].size() << " stairs." << endl;
	}

	for (auto& row : ways) {
		if (ways.size() >= 10 && counter < 10) {
			cout << " " << counter << ". [";
		} else {
			cout << counter << ". [";
		}
		for (auto& col : row) {
			count += col;
			if (count == max) {
				cout << col;
			} else {
				cout << col << ", ";
			}
		}
		counter += 1;
		cout << "]" << endl;
		count = 0;
	}
}

int main(int argc, char * const argv[]) {
	int m;
	istringstream iss;

	if (argc != 2) {
		cerr << "Usage: " << argv[0] << " <number of stairs>" << endl;
		return 1;
	}

	iss.str(argv[1]);
	if ( (!(iss >> m)) || (m <= 0)) {
		cerr << "Error: Number of stairs must be a positive integer." << endl;
		return 1;
	}

	//int i = atoi (argv[1]);
	//get_ways(m);

	vector< vector<int> > combos = get_ways(m);
	display_ways(combos);


	return 0;
}
