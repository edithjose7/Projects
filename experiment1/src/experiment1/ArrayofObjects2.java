package experiment1;
public class ArrayofObjects2 {
	public static void main(String args[]) {

        int[] Array = {35, 12, 39, 18, 55, 64, 73, 17, 88, 27};
        int N = Array.length;

        int[] ascendingArray = new int[N];
        int[] descendingArray = new int[N];

        for (int i = 0; i < N; i++) {
            ascendingArray[i] = Array[i];
            descendingArray[i] = Array[i];
        }

        sortAscending(ascendingArray);
        sortDescending(descendingArray);

        System.out.print("Ascending Order: ");
        printArray(ascendingArray);

        System.out.print("Descending Order: ");
        printArray(descendingArray);
    }


    static void sortAscending(int[] array) {
        int n = array.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    // Swap array[j] and array[j + 1]
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    static void sortDescending(int[] array) {
        int n = array.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] < array[j + 1]) {
                    // Swap array[j] and array[j + 1]
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

}
