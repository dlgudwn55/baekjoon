import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		String target = "SciComLove";
		
		Scanner sc = new Scanner(System.in);
		
		String input = sc.nextLine();
		int ans = 0;
		String a, b;
		for (int i=0; i<10; i++) {
			if (input.charAt(i) != target.charAt(i))
				ans++;
		}
		System.out.println(ans);
	}

}
