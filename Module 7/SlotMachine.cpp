/*****
 * Author: Glowstudent
 * Program: Slot Machine
 *****/

#include <iostream>
#include <string>
#include <iomanip>
#include <limits>
#include <random>

using namespace std;

int moneyTemp = 0;
int moneyTotal = 0;
int betTemp = 0;
int betTotal = 0;

int random(int min, int max)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(min, max);

    return dis(gen);
}

int spinSlots()
{
    int spin = random(1, 6);

    switch (spin)
    {
    case 1:
        cout << "Cherries";
        return 1;
        break;
    case 2:
        cout << "Oranges";
        return 2;
        break;
    case 3:
        cout << "Plums";
        return 3;
        break;
    case 4:
        cout << "Bells";
        return 4;
        break;
    case 5:
        cout << "Melons";
        return 5;
        break;
    case 6:
        cout << "Bars";
        return 6;
        break;
    default:
        cout << "Error";
        return 0;
        break;
    }
}

void playSlots()
{
    bool isInvalid = true;
    do
    {
        cout << "Enter amount to bet: ";
        cin >> betTemp;

        // Check if input is numeric
        if (cin.fail())
        {
            cout << "Invalid input. Please enter a number." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else
        {
            if (betTemp <= 0)
                cout << "Invalid input. Bet must be greater than 0." << endl;
            else
                isInvalid = false;
        }
    } while (isInvalid);

    cout << "Spinning the wheels..." << endl;

    cout << "| ";
    int slot1 = spinSlots();
    cout << " | ";
    int slot2 = spinSlots();
    cout << " | ";
    int slot3 = spinSlots();
    cout << " |" << endl;

    if (slot1 == slot2 && slot2 == slot3)
    {
        cout << "You win $" << betTemp * 3 << "!" << endl;
        moneyTemp += betTemp * 3;
    }
    else if (slot1 == slot2 || slot2 == slot3 || slot1 == slot3)
    {
        cout << "You win $" << betTemp * 2 << "!" << endl;
        moneyTemp += betTemp * 2;
    }
    else
    {
        cout << "You lost $" << betTemp << "!" << endl;
        moneyTemp = 0;
    }

    moneyTotal += moneyTemp;
    betTotal += betTemp;

    moneyTemp = 0;
    betTemp = 0;
}

int main()
{
    char playAgain;

    cout << "Welcome to the Slot Machine!" << endl;

    do
    {
        playSlots();

        cout << "Do you want to play again? (y/n): ";
        cin >> playAgain;
    } while (playAgain == 'y' || playAgain == 'Y');

    cout << "You bet a total of $" << betTotal << " and won a total of $" << moneyTotal << "." << endl;

    return 0;
}