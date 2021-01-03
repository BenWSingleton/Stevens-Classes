/*******************************************************************************
 * Name    : sieve.cpp
 * Author  : Benjamin Singleton
 * Version : 1.0
 * Date    : September 18, 2020
 * Description : Finds prime numbers using the sieve of Eratosthenes.
 * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
 ******************************************************************************/
#include <iostream>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <sstream>

using namespace std;

class PrimesSieve {
public:
    PrimesSieve(int limit);

    ~PrimesSieve() {
        delete [] is_prime_;
    }

    int num_primes() const {
        return num_primes_;
    }

    void display_primes() const;

private:
    // Instance variables
    bool * const is_prime_;
    const int limit_;
    int num_primes_, max_prime_;

    // Method declarations
    int count_num_primes() const;
    int find_max_primes() const;
    void sieve();
    static int num_digits(int num);
};

PrimesSieve::PrimesSieve(int limit) :
        is_prime_{new bool[limit + 1]}, limit_{limit} {
    sieve();
}

void PrimesSieve::display_primes() const {
    // TODO: write code to display the primes in the format specified in the
    // requirements document.

	const int max_prime_width = num_digits(max_prime_);
	const int primes_per_row = 80 / (max_prime_width + 1);
	int row_count = 0;

	//cout << "max_prime_width: " << max_prime_width << endl;
	//cout << "primes_per_row: " << primes_per_row << endl;
	//cout << "max_prime: " << max_prime_ << endl;
	//cout << "num_primes: " << num_primes_ << endl;

	cout << "Number of primes found: " << num_primes_ << endl;
	cout << "Primes up to " << limit_ << ":" << endl;
	if (num_primes_ > primes_per_row) {
		for (int i = 1; i < limit_ + 1; i++) {
			if (is_prime_[i]==true) {
				if (i == max_prime_ || (row_count+1) >= primes_per_row) { //Checks for final prime and doesn't add space
					cout << setw(max_prime_width) << i;
				} else {
					cout << setw(max_prime_width) << i << " ";
				}
				row_count++;
				if (row_count >= primes_per_row) {
					cout << endl;
					row_count = 0;
				}
			}
		}
	} else {
		for (int i = 1; i < limit_ + 1; i++) {
			if (is_prime_[i]==true) {
				if (i == max_prime_) {
					cout << i;
				} else {
					cout << i << " ";
				}
			}
		}
	}
	cout << endl;
}

int PrimesSieve::count_num_primes() const {
    // TODO: write code to count the number of primes found
	int count = 0;
	for (int i = 2; i < limit_ + 1; i++) {
		if (is_prime_[i] == true) {
			count++;
		}
	}
    return count;
}

int PrimesSieve::find_max_primes() const {
	//Finds and returns largest prime number by going backwards through is_prime_
	for (int i = limit_; i >= 2; i-- ) {
		if (is_prime_[i]==true) {
			return i;
			break;
		}
	}
	return 1;
}

void PrimesSieve::sieve() {
    // TODO: write sieve algorithm
	for (int i = 2; i < limit_ + 1; i++) {
		is_prime_[i]=true;
	}
	//is_prime_[0]=false;
	//is_prime_[1]=false;
	//is_prime_[2]=true;

	for (int i = 2; i <= sqrt(limit_ + 1); i++) {
		if (is_prime_[i] == true) {
			for (int j = pow(i, 2); j <= limit_ + 1; j+=i) {
				is_prime_[j] = false;
			}
		}
	}

	max_prime_ = find_max_primes();
	num_primes_ = count_num_primes();
}

int PrimesSieve::num_digits(int num) {
    // TODO: write code to determine how many digits are in an integer
    // Hint: No strings are needed. Keep dividing by 10.
	int count = 0;
	while (num >= 1) {
		num = num/10;
		count = count + 1;
	}
    return count;
}

int main() {
    cout << "**************************** " <<  "Sieve of Eratosthenes" <<
            " ****************************" << endl;
    cout << "Search for primes up to: ";
    string limit_str;
    cin >> limit_str;
    int limit;

    // Use stringstream for conversion. Don't forget to #include <sstream>
    istringstream iss(limit_str);

    // Check for error.
    if ( !(iss >> limit) ) {
        cerr << "Error: Input is not an integer." << endl;
        return 1;
    }
    if (limit < 2) {
        cerr << "Error: Input must be an integer >= 2." << endl;
        return 1;
    }

    // TODO: write code that uses your class to produce the desired output.
    cout << endl;
    PrimesSieve Sieve(limit);
    Sieve.display_primes();
    return 0;
}
