import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Main {
	public static boolean checkIncrease(int[] arr, int skipIdx) {
		if (arr[skipIdx-1] > arr[skipIdx+1])
			return false;
		
		for (int i=0; i<skipIdx-1; i++)
			if (arr[i] > arr[i+1])
				return false;
		
		for (int i=skipIdx+1; i<arr.length-1; i++)
			if (arr[i] > arr[i+1])
				return false;
		
		return true;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			int g = sc.nextInt();
			int[] gids = new int[g];
			for (int j=0; j<g; j++) {
				gids[j] = sc.nextInt();
			}

			int ans = 0;
			for (int j=1; j<g-1; j++) {
				if(checkIncrease(gids, j)) {
					ans = j + 1;
					break;
				}
				
			}
			System.out.println(ans);
		}
		
	}
}
