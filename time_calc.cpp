#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int sum = 0;
    double input;

    do {
        cout << "Enter your duration: ";
        cin >> input;
        sum += floor(input) * 60 + (input - floor(input)) * 100;
    } while (input != 0);

    cout << floor(sum / 60) + (sum % 60)/100.0 << endl;
}