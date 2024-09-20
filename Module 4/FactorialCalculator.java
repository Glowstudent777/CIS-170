/*****
* Author: Glowstudent
* Program: Factorial Calculator
*****/

import java.util.Scanner;

public class FactorialCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int input;
	    int max_input = 16;
        int factorial = 1;

        System.out.print("Enter any number up to 16: ");
        input = sc.nextInt();

        while (input > max_input) {
            System.out.print("Number is too large. Pick another number: ");
            input = sc.nextInt();
        }

        for (int i = 1; i <= input; i++) {
            factorial *= i;
        }

        System.out.printf("The factorial of %s is %s", input, factorial);
    }
}