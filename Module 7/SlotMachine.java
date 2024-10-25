/*****
* Author: Glowstudent
* Program: Slot Machine
*****/

import java.util.Scanner;

public class SlotMachine {

    public static int moneyTotal = 0;
    public static int betTotal = 0;

    private static final String[] symbols = { "Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars" };

    private static void playSlots() {
        boolean isInvalid = true;
        int tempBet = 0;
        int moneyTemp = 0;

        Scanner sc = new Scanner(System.in);

        while (isInvalid) {
            System.out.print("Enter amount to bet: ");
            String userInput = sc.nextLine();
            try {
                tempBet = Integer.parseInt(userInput);
                if (tempBet > 0) {
                    isInvalid = false;
                } else {
                    System.out.println("Invalid bet amount. Please enter a positive number.");
                    isInvalid = true;
                }
            } catch (Exception ignored) {
                System.out.println("Invalid bet amount. Please enter a positive number.");
                isInvalid = true;
            }
        }

        String[] slots = new String[3];
        for (int i = 0; i < slots.length; i++) {
            slots[i] = symbols[(int) (Math.random() * symbols.length)];
        }

        System.out.printf("%s %s %s\n", slots[0], slots[1], slots[2]);

        if (slots[0].equals(slots[1]) && slots[1].equals(slots[2])) {
            System.out.println("You won $" + (tempBet * 3) + "!");
            moneyTemp += tempBet * 3;
        } else if (slots[0].equals(slots[1]) || slots[1].equals(slots[2]) || slots[0].equals(slots[2])) {
            System.out.println("You won $" + (tempBet * 2) + "!");
            moneyTemp += tempBet * 2;
        } else {
            System.out.println("You lost $" + tempBet + ".");
        }

        moneyTotal += moneyTemp;
        betTotal += tempBet;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to the Slot Machine!");

        while (true) {
            playSlots();

            System.out.print("Would you like to play again? (y/n): ");
            String input = sc.nextLine().toLowerCase();
            if (!input.equals("y"))
                break;
        }

        System.out.println("You have bet a total of $" + betTotal + " and won a total of $" + moneyTotal);
    }
}