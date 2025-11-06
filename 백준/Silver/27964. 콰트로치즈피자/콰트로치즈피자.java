import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.nextLine();
		String input = sc.nextLine();
		String[] toppings = input.split(" ");
		
		Set<String> set = new HashSet<>();
		for (String topping : toppings) {
			if (topping.endsWith("Cheese")) {
				set.add(topping);
			}
		}
		if (set.size() >= 4) {
			System.out.println("yummy");
		}
		else {
			System.out.println("sad");
		}
	}
}
