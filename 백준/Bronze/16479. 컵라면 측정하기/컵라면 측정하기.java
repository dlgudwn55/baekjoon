import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int k = sc.nextInt();
		int d1 = sc.nextInt();
		int d2 = sc.nextInt();
		
		double tmp = (double)(d1 - d2) / 2;
		System.out.println(Math.pow(k, 2) - Math.pow(tmp, 2));
	}
}
