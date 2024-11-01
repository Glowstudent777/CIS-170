/*****
 * Author: Glowstudent
 * Program: Siblings
 *****/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int uInput;

    cout << "Enter number of siblings: ";
    cin >> uInput;

    if (cin.fail() || uInput < 0)
    {
        cout << "Invalid entry for number of siblings! Program is exiting!" << endl;
        return 1;
    }

    if (uInput == 0)
    {
        cout << "Ah you are the only child." << endl;
    }
    else
    {
        vector<string> siblings(uInput);
        cin.ignore();
        for (int i = 0; i < uInput; i++)
        {
            cout << "Enter sibling number " << i + 1 << " name: ";
            getline(cin, siblings[i]);
        }

        cout << "\nYour siblings are:\n";
        for (int i = 0; i < uInput; i++)
        {
            cout << siblings[i] << endl;
        }
    }
    return 0;
}