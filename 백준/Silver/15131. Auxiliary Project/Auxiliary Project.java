import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

//		int[] two = { 1 };
//		int[] three = { 7 };
//		int[] four = { 4 };
//		int[] five = { 5, 3, 2 };
//		int[] six = { 9, 6, 0 };
//		int[] seven = { 8 };

		int n = sc.nextInt();

		Map<Integer, Integer> map = new HashMap<>();
		map.put(2, 1);
		map.put(3, 7);
		map.put(4, 4);
		map.put(5, 8);
		map.put(6, 14);
		map.put(7, 11);
		map.put(8, 15);
		
		if (n<=7) {
			System.out.println(map.get(n));
			return;
		}
		for (int i=9; i<=n; i++) {
			map.put(i, 0);
			for (int j=2; j<=7; j++) {
				int tmp = map.get(j) + map.get(i-j);
				if (tmp > map.get(i))
					map.replace(i, tmp);
			}
		}
		System.out.println(map.get(n));
	}
}
