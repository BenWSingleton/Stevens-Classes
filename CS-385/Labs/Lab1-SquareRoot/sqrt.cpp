/*******************************************************************************
 * Name    : sqrt.cpp
 * Author  : Benjamin Singleton
 * Version : 1.0
 * Date    : September 3, 2020
 * Description : Computes the square root of a double using Newton's method.
 * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
 ******************************************************************************/
#include <iostream>
#include <sstream>
#include <limits>
#include <iomanip>
using namespace std;

double sqrt(double num, double epsilon = .0000001) {
	// cerr << "square root";
	// cerr << num;
	//cerr << "  ";
	//cerr << epsilon;
	//cerr << " ";

	if (num < 0) {
		numeric_limits<double>::quiet_NaN();
	}

	if (num == 0 || num == 1) {
		return num;
	}

	double last_guess = num;
	double next_guess = (last_guess + (num/last_guess))/2;
	//double temp = 0;

	while (abs(last_guess-next_guess) > epsilon) {
		//temp = next_guess;
		last_guess = next_guess;
		next_guess = (last_guess + (num/last_guess))/2;
		//last_guess = temp;
		//cerr << temp;
		//cerr << last_guess;
		//cerr << next_guess;
	}

	return next_guess;
}

int main(int argc, char *argv[]) {
	double m, n;
	istringstream iss;

	if (argc > 3 || argc == 1) {
		cerr << "Usage: " << argv[0] << " <value> [epsilon]" << endl;
		return 1;
	}

	iss.str(argv[1]);
	if ( !(iss >> m) ) {
		cerr << "Error: Value argument must be a double." << endl;
		return 1;
	}

	if (m < 0.0) {
		cerr << numeric_limits<double>::quiet_NaN() << endl;
		return 1;
	}

	if (argc == 3) {
		iss.clear();
		iss.str(argv[2]);
		if ( !(iss >> n)) {
			cerr << "Error: Epsilon argument must be a positive double." << endl;
			return 1;
		}
		if (n <= 0) {
			cerr << "Error: Epsilon argument must be a positive double." << endl;
			return 1;
		}
		// cerr << "Epsilon given" << endl;
		cout << fixed << setprecision(8) << sqrt(m, n) << endl;
		return 0;
	}

	// cerr << "No epsilon" << endl;
	cout << fixed << setprecision(8) << sqrt(m) << endl;
	return 0;

}

