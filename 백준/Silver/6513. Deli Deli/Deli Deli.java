import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String vowels = "aeiou";
		
		int l = sc.nextInt();
		int n = sc.nextInt();
		
		Map<String, String> plurals = new HashMap<>();
		for (int i=0; i<l; i++) {
			String s = sc.next();
			String p = sc.next();
			plurals.put(s, p);
		}
		
		for (int i=0; i<n; i++) {
			String food = sc.next();
			if (plurals.containsKey(food)) {
				System.out.println(plurals.get(food));
			} else if (food.charAt(food.length()-1) == 'y' && vowels.indexOf(food.charAt(food.length()-2)) == -1) {
				System.out.println(food.substring(0, food.length()-1) + "ies");
			} else if (
					food.substring(food.length()-1, food.length()).equals("o") ||
					food.substring(food.length()-1, food.length()).equals("s") ||
					food.substring(food.length()-1, food.length()).equals("x") ||
					food.substring(food.length()-2, food.length()).equals("ch") ||
					food.substring(food.length()-2, food.length()).equals("sh")
					) {
				System.out.println(food + "es");
			} else {
				System.out.println(food + "s");
			}
		}
		
	}
}
