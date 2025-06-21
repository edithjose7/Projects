package experiment1;

public class ControlStatements3 {
	public static void main(String args[]) {
        int n = 4;  //Number of rows

        for (int i = 1; i <= n; i++) {
            for (int j = n - i; j > 0; j--) {
                System.out.print(" ");
            }
            // Print stars
            for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

}
