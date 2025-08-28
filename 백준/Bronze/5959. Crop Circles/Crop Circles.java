import java.util.Scanner;

class Circle {
	int x;
	int y;
	int r;
	
	Circle(int x, int y, int r) {
		this.x = x;
		this.y = y;
		this.r = r;
	}
}

class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		Circle[] circles = new Circle[n];
		int x, y, r;
		for (int i=0; i<n; i++) {
			x = sc.nextInt();
			y = sc.nextInt();
			r = sc.nextInt();
			circles[i] = new Circle(x, y, r);
		}
		
		int ans, dist_squared;
		Circle c1, c2;
		for (int i=0; i<n; i++) {
			ans = 0;
			c1 = circles[i];
			for (int j=0; j<n; j++) {
				if (i == j) continue;
				c2 = circles[j];
				dist_squared = (int) Math.pow(c1.x - c2.x, 2) + (int) Math.pow(c1.y - c2.y, 2);
				if (dist_squared < Math.pow((c1.r + c2.r), 2)) ans++;
			}
			System.out.println(ans);
		}
		
	}
}
