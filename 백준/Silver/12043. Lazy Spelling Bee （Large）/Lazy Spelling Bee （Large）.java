import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Main {
	public static void main(String[] args) {
		final long DIV = 1000000007;
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for (int tn=1; tn<=t; tn++) {
			String input = sc.next();
			if (input.length() == 1) {
				System.out.println("Case #" + tn + ": " + 1);
				continue;
			}
			if (input.length() == 2) {
				if (input.charAt(0) == input.charAt(1)) {
					System.out.println("Case #" + tn + ": " + 1);
					continue;
				} else {
					System.out.println("Case #" + tn + ": " + 4);
					continue;
				}
			}
			long ans = (input.charAt(0) == input.charAt(1)) ? 1 : 2;
			for (int i=1; i<input.length()-1; i++) {
				Set<Character> set = new HashSet<>();
				set.add(input.charAt(i-1));
				set.add(input.charAt(i));
				set.add(input.charAt(i+1));
				ans = (ans % DIV) * (set.size() % DIV) % DIV;
			}
			ans *= (input.charAt(input.length()-2) == input.charAt(input.length()-1)) ? 1 : 2;
			System.out.println("Case #" + tn + ": " + (ans % DIV));
		}
		
	}
}
