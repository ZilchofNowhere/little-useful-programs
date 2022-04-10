#include <iostream>
using namespace std;

enum Numeral {
    M = 1000,
    D = 500,
    C = 100,
    L = 50,
    X = 10,
    V = 5,
    I = 1
};

void addNumeral(Numeral numeral, string& result, int& number) {
    switch (numeral) {
        case 1000:
            result += "M";
            break;
        
        case 500:
            result += "D";
            break;

        case 100:
            result += "C";
            break;

        case 50:
            result += "L";
            break;

        case 10:
            result += "X";
            break;

        case 5:
            result += "V";
            break;

        case 1:
            result += "I";
            break;

        default:
            break;
    }
    number -= numeral;
}

int main(){
    int num;
    string result{""};
    cout << "Enter the number to be converted: ";
    cin >> num;
    while (num != 0) {
        if (num / 1000 > 0) {
            for (int i = 0; i < num / 1000; i++){
                addNumeral(M, result, num);
            }
        }
        else if (num / 500 > 0) {
            if (num > 899) {
                addNumeral(C, result, num);
                result += "M";
                num %= 100;
            }
            else {
                for (int i = 0; i < num / 500; i++){
                    addNumeral(D, result, num);
                }
            }
        }
        else if (num / 100 > 0) {
            if (num > 399) {
                addNumeral(C, result, num);
                result += "D";
                num %= 100;
            } else {
                for (int i = 0; i < num / 100; i++){
                    addNumeral(C, result, num);
                }
            }
        }
        else if (num / 50 > 0) {
            if (num > 89) {
                addNumeral(X, result, num);
                result += "C";
                num %= 10;
            } else {
                addNumeral(L, result, num);
                for (int i = 0; i < num / 10; i++) {
                    addNumeral(X, result, num);
                }
            }
        }
        else if (num / 10 > 0) {
            if (num > 39) {
                addNumeral(X, result, num);
                result += "L";
                num %= 10;
            } else {
                for (int i = 0; i < num / 10; i++) {
                    addNumeral(X, result, num);
                }
            }
        }
        else if (num / 5 > 0) {
            if (num > 8) {
                addNumeral(I, result, num);
                result += "X";
                num = 0;
            } else {
                addNumeral(V, result, num);
                for (int i = 0; i < num / 10; i++) {
                    addNumeral(I, result, num);
                }
            }
        }
        else {
            if (num > 3) {
                addNumeral(I, result, num);
                result += "V";
                num = 0;
            } else {
                for (int i = 0; i < num; i++) {
                    addNumeral(I, result, num);
                }
            }
        }
    }

    cout << "The representation of your number with the Roman numerals is " << result << "." << endl;
}