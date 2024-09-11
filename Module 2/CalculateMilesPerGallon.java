/*****
* Author: Glowstudent
* Program: Calculate Miles-Per-Gallon
*****/

import java.util.Scanner;

public class CalculateMilesPerGallon {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int milesDriven;
		int gallonsUsed;
		float milesPerGallon;
		
		System.out.print("Enter number of miles driven (round to nearest mile): ");
		milesDriven = sc.nextInt();
		
		System.out.print("Enter gallons of gas used (round to the nearest gallon): ");
		gallonsUsed = sc.nextInt();
		
		milesPerGallon = (float) milesDriven / gallonsUsed;
		System.out.printf("Estimated miles-per-gallon: %.2f", milesPerGallon);
	}
}