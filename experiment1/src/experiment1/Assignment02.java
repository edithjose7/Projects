package experiment1;

public class Assignment02 {
	public static void main(String[] args) {
        String input = "I love programming very much";

        String[] words = input.split(" ");
        
        int left = 0;
        int right = words.length - 1;
        while (left < right) {
            String temp = words[left];
            words[left] = words[right];
            words[right] = temp;

            left++;
            right--;
        }

        String reversed = String.join(" ", words);
        
        System.out.println(input);
        System.out.println(reversed);
    }

}
