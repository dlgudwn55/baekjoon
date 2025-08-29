import java.util.Scanner;

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		boolean[][] field = new boolean[501][501];
		
		int x1, y1, x2, y2;
		for (int i=0; i<n; i++) {
			x1 = sc.nextInt();
			y1 = sc.nextInt();
			x2 = sc.nextInt();
			y2 = sc.nextInt();
			
			for (int r=x1; r<x2; r++) {
				for (int c=y1; c<y2; c++) {
					field[r][c] = true;
				}
			}
		}
		
		int ans = 0;
		for (int r=0; r<501; r++) {
			for (int c=0; c<501; c++) {
				if (field[r][c])
					ans++;
			}
		}
		
		System.out.println(ans);
		
	}
}
