// Author: Glowstudent
// Program: Leap Year Detector

import java.util.Scanner;

public class CalculateMilesPerGallon {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int year;
		
		System.out.print("Enter a year to see if it is a leap year: ");
		year = sc.nextInt();
		
		if (year % 400 == 0)
         System.out.printf("% is a leap year", year);
      else if (year % 100 != 0 && year % 4 == 0)
        System.out.printf("% is a leap year", year);
      else
        System.out.printf("% is not a leap year", year);
	}
}