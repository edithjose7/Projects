package experiment1;

public class ArrayofObjects1 {
	public static void main(String args[]) {
        char[] arr = {'a', 'b', 'c', 'a', 'd', 'e', 'b', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'};
       
        Duplicate(arr);
        VowelsAndConsonants(arr);
    }

    static void Duplicate(char[] arr) {
        System.out.println("Duplicate characters:");
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    System.out.println(arr[i]);
                    break;
                }
            }
        }
    }

    static void VowelsAndConsonants(char[] arr) {
        int vowels = 0;
        int consonants = 0;

        for (int i = 0; i < arr.length; i++) {
            char ch = arr[i];
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
                ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                vowels++;
            } else if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                consonants++;
            }
        }

        System.out.println("Number of vowels: " + vowels);
        System.out.println("Number of consonants: " + consonants);
    }
	

}
