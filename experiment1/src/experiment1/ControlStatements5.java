package experiment1;

import java.util.Scanner;

public class ControlStatements5 {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Menu:");
        System.out.println("1. Check if the number is a Buzz number");
        System.out.println("2. Check if the number is even or odd");
        System.out.println("3. Check if the number is positive or negative");
        System.out.print("Enter your choice (1-3): ");
        int choice = sc.nextInt();

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        switch (choice) {
            case 1:
                // Check if the number is a Buzz number
                if (number % 7 == 0||number % 10 == 7) {
                    System.out.println(number + " is a Buzz number.");
                } else {
                    System.out.println(number + " is not a Buzz number.");
                }
                break;
            case 2:
                // Check if the number is even or odd
                if (number % 2 == 0) {
                    System.out.println(number + " is even.");
                } else {
                    System.out.println(number + " is odd.");
                }
                break;
            case 3:
                // Check if the number is positive or negative
                if (number > 0) {
                    System.out.println(number + " is positive.");
                } else if (number == 0) {
                    System.out.println(number + " is neither positive nor negative.");
                } else {
                    System.out.println(number + " is negative.");
                }
                break;
            default:
                System.out.println("Invalid choice. Please enter a number between 1 and 3.");
                break;
        }

       
        sc.close();
    }

}
