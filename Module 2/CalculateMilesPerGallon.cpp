/*****
* Author: Glowstudent
* Program: Calculate Miles Per Gallon
*****/

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{

	// Declare variables
	int milesDriven, gallonsUsed;
	float milesPerGallon;
	
	// Get the miles driven
	cout << "Enter number of miles driven (round to nearest mile): ";
	cin >> milesDriven;
	
	// Get the gallons used
	cout << "Enter gallons of gas used (round to the nearest gallon): ";
	cin >> gallonsUsed;
	
	// Calculate the miles per gallon
	milesPerGallon = (float) milesDriven / (float) gallonsUsed;
	
	// Display the miles per gallon
	cout << "Estimated miles-per-gallon: " << setprecision(2) << fixed <<
	milesPerGallon << endl;
	
	return 0;
}