/*****
* Author: Glowstudent
* Program: Template
*****/

import java.util.Scanner;

public class Template {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input;

        System.out.print("Enter your name: ");
        input = sc.nextLine();

        System.out.printf("Hello, %s!", input);
    }
}