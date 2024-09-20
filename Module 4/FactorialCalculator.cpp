/*****
* Author: Glowstudent
* Program: Factorial Calculator
*****/

#include <iostream>

using namespace std;

int main()
{
	int input;
	int max_input = 16;

	cout << "Enter any number up to 16: ";
	cin >> input;

	while (input > max_input)
	{
		cout << "Number is too large. Pick another number: ";
		cin >> input;
	}

	int i = 0, count;
	while (i < input) {
		if (i == 0) count = ++i;
		else count *= ++i;
	}

	cout << "The factorial is: " << count << endl;

	return 0;
}