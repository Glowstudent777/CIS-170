/*****
 * Author: Glowstudent
 * Program: Kilometer Converter
 *****/

#include <iostream>
#include <string>

using namespace std;

void kilometerToMiles(float kilometers, float &miles);

int main()
{
    float kilometers, miles;

    cout << "Enter the number of kilometers to convert to miles: ";
    cin >> kilometers;

    kilometerToMiles(kilometers, miles);

    cout << kilometers << " kilometers is approximately " << miles << " miles." << endl;

    return 0;
}

void kilometerToMiles(float kilometers, float &miles)
{
    miles = kilometers * 0.6214;
}