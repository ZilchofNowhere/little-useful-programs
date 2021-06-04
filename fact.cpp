#include <iostream>
#include <windows.h>
#include <thread>
#include <chrono>
using namespace std;

void fact(int num){
    int a = 1;
    for (int i = 1; i <= num; ++i){
        a*=i;
    }
    cout << "Factorial of your number is " << a;
}

int main(){
    int x; cout << "Enter your number:\n"; cin >> x; fact(x);
    printf("\nMission complete. Press x to quit.\n");
    string s;
    cin >> s;
    if (s == "x"){
        return 0;
    } else {
        cout << "Wrong key. Quitting in 2 seconds anyway.";
        Sleep(2000);
        return 0;
    }
}
