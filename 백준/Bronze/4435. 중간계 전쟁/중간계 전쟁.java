import java.util.Scanner;

class Main {
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		int[] gan = new int[6];
		int[] sau = new int[7];
		
		int[] arr1 = {1,2,3,3,4,10};
		int[] arr2 = {1,2,2,2,3,5,10};
		
		for (int i=1; i<=t; i++) {
			
			for (int j=0; j<6; j++) {
				gan[j] = sc.nextInt();
			}
			for (int j=0; j<7; j++) {
				sau[j] = sc.nextInt();
			}
			
			int ganScore = 0;
			int sauScore = 0;
			
			for (int j=0; j<6; j++) {
				ganScore += arr1[j]*gan[j];
			}
			for (int j=0; j<7; j++) {
				sauScore += arr2[j]*sau[j];
			}
			
			if (ganScore > sauScore)
				System.out.println("Battle " + i + ": Good triumphs over Evil");
			else if (ganScore < sauScore)
				System.out.println("Battle " + i + ": Evil eradicates all trace of Good");
			else
				System.out.println("Battle " + i + ": No victor on this battle field");
		}
	}
}
