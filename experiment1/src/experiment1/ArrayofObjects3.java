package experiment1;

import java.util.*;

public class ArrayofObjects3 {
	public static void main(String args[]) {
        String[] Array = {"listen", "silent", "enlist", "hello", "silent", "world"};

        Anagrams(Array);
    }

    static void Anagrams(String[] Array) {
        List<String> checked = new ArrayList<>();
        for (int i = 0; i < Array.length; i++) {
            if (!checked.contains(Array[i])) {
                List<String> anagrams = new ArrayList<>();
                for (int j = 0; j < Array.length; j++) {
                    if (i != j && !checked.contains(Array[j]) && areAnagrams(Array[i], Array[j])) {
                        anagrams.add(Array[j]);
                        checked.add(Array[j]);
                    }
                }
                if (!anagrams.isEmpty()) {
                    anagrams.add(Array[i]);
                    System.out.println("Anagrams: " + anagrams);
                }
            }
        }
    }

    static boolean areAnagrams(String str1, String str2) {
        // Convert strings to char arrays
        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();

        // Check if lengths are different
        if (arr1.length != arr2.length) {
            return false;
        }

        // Sort and compare the arrays
        sortArray(arr1);
        sortArray(arr2);

        // Check if sorted arrays are equal
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }

    // Method to sort a char array in ascending order using bubble sort
    public static void sortArray(char[] array) {
        int n = array.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    // Swap array[j] and array[j + 1]
                    char temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

}
