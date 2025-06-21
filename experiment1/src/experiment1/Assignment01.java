package experiment1;

import java.util.*;

public class Assignment01 {
	public static void main(String[] args) {
        String s1 = "abc";
        int k1 = 2;
        System.out.println("Input: " + s1 + ", k = " + k1);
        System.out.println("Possible substrings are " + countSubstrings(s1, k1));

        String s2 = "aba";
        int k2 = 2;
        System.out.println("Input: " + s2 + ", k = " + k2);
        System.out.println("Possible substrings are " + countSubstrings(s2, k2));
    }

    public static String countSubstrings(String s, int k) {
        int n = s.length();
        StringBuilder result = new StringBuilder();  // StringBuilder to store the result substrings

        // Outer loop to set the starting point of the substring
        for (int i = 0; i < n; i++) {
            Map<Character, Integer> charCount = new HashMap<>();  // Map to count character frequencies
            int diffCount = 0;  // Counter for distinct characters in the current substring

            // Inner loop to extend the substring
            for (int j = i; j < n; j++) {
                char c = s.charAt(j);  // Current character

                // Add the character to the map and update its frequency
                charCount.put(c, charCount.getOrDefault(c, 0) + 1);

                // If it's the first time we've seen this character, increment the distinct count
                if (charCount.get(c) == 1) {
                    diffCount++;
                }

                // Check if the current substring has exactly k distinct characters
                if (diffCount == k) {
                    result.append("\"").append(s.substring(i, j + 1)).append("\", ");
                } else if (diffCount > k) {
                    break;
                }
            }
        }

        // Remove the trailing comma and space, if present
        if (result.length() > 0) {
            result.setLength(result.length() - 2);
        }

        return "{" + result.toString() + "}";
    }

}
