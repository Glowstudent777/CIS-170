
/** ***
 * Author: Glowstudent
 * Program: Siblings
 **** */
import java.util.Scanner;

public class Siblings {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int uInput;

        try {

            System.out.print("Enter number of siblings: ");
            uInput = sc.nextInt();

            if (uInput >= 0) {
                if (uInput == 0) {
                    System.out.print("Ah you are an only child.");
                } else {
                    String[] siblings = new String[uInput];

                    sc.nextLine();

                    for (int i = 0; i < uInput; i++) {
                        System.out.print("Enter sibling number " + (i + 1) + " name: ");
                        siblings[i] = sc.nextLine();
                    }

                    System.out.println("\nYour siblings are:");
                    for (int i = 0; i < uInput; i++) {
                        System.out.println(siblings[i]);
                    }
                }
            } else {
                System.out.println("Invalid entry for number of siblings! Program is exiting!");
            }

        } catch (Exception ignored) {
            System.out.println("Invalid entry for number of siblings! Program is exiting!");
        }

        sc.close();
    }
}
