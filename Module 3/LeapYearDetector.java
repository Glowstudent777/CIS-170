/*****
* Author: Glowstudent
* Program: Leap Year Detector
*****/

import java.util.Scanner;

public class LeapYearDetector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int year;

        System.out.print("Enter a year to see if it is a leap year: ");
        year = sc.nextInt();

        if ((float) year % 400 == 0)
            System.out.printf("%s is a leap year", year);
        else if ((float) year % 100 != 0 && year % 4 == 0)
            System.out.printf("%s is a leap year", year);
        else
            System.out.printf("%s is not a leap year", year);
    }
}