#include <iostream>
#include <string>
#include <list>
using namespace std;

int p1 = 1;
int p2 = 2;
string board = {
    "1   2   3\n"
    "4   5   6\n"
    "7   8   9\n"
};
/* 
    * key indices:
    -  0,  4,  8
    - 10, 14, 18
    - 20, 24, 28
*/
int winner;
bool boardCompare(int i, int j, int k, char s){
    if (board[i] == board[j]){
        if (board[i] == board[k]){
            if (board[i] == s){
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

int main(){
    bool isOver = false;
    int move;
    list<int> availableMoves = {1,2,3,4,5,6,7,8,9};
    int curp = p1;

    cout << "Welcome to this competitive game of Tic-Tac-Toe!" << endl;
    
    while (isOver == false){
        if (curp == p1){
            cout << "Player 1's turn!" << endl;
        } else {
            cout << "Player 2's turn!" << endl;
        }

        cout << "Current situation of the board:" << endl;
        cout << board << endl;
        cout << "Enter the number at the cell where you want to put your symbol:" << endl;
        try {    
            cin >> move;
        } catch (exception){
            cout << "Invalid input. Please try again." << endl;
            move = 0;
        }
        
        bool isAvail;
        for (int i : availableMoves){
            if (i == move){
                isAvail = true;
                break;
            } else {
                isAvail = false;
                continue;
            }
        }

        if (move <= 9 && isAvail == true){
            string mv = to_string(move);
            if (curp == p1){
                board[board.find(mv)] = 'X';
                curp = p2;
            } else {
                board[board.find(mv)] = 'O';
                curp = p1;
            }
            availableMoves.remove(move);
        } else {
            cout << "Invalid input. Please try again." << endl;
        }

        if (
            boardCompare(0, 4, 8, 'X') ||
            boardCompare(10, 14, 18, 'X') ||
            boardCompare(20, 24, 28, 'X') ||
            boardCompare(0, 10, 20, 'X') ||
            boardCompare(4, 14, 24, 'X') ||
            boardCompare(8, 18, 28, 'X') ||
            boardCompare(0, 14, 28, 'X') ||
            boardCompare(8, 14, 20, 'X')
        ){
            winner = p1;
            isOver = true;
        } else if (
            boardCompare(0, 4, 8, 'X') ||
            boardCompare(10, 14, 18, 'X') ||
            boardCompare(20, 24, 28, 'X') ||
            boardCompare(0, 10, 20, 'X') ||
            boardCompare(4, 14, 24, 'X') ||
            boardCompare(8, 18, 28, 'X') ||
            boardCompare(0, 14, 28, 'X') ||
            boardCompare(8, 14, 20, 'X')
        ){
            winner = p2;
            isOver = true;
        } else {
            winner = 0;
        }

        if (availableMoves.size() == 0){
            isOver = true;
        }
    }
    cout << board << endl;
    cout << "* APPLAUSE *" << endl;
    
    if (winner == p1){
        cout << "Player 1 won! Good game!" << endl; 
    } else if (winner == p2) {
        cout << "Player 2 won! Good game!" << endl; 
    } else {
        cout << "It's a draw! Good game!" << endl;
    }
    
    system("pause");
}
