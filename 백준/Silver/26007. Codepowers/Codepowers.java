import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main {
	public static void main(String[] args) throws Exception {
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
				
		String line = br.readLine();
		String[] nums = line.split(" ");
		int n = Integer.parseInt(nums[0]);
		int m = Integer.parseInt(nums[1]);
		int k = Integer.parseInt(nums[2]);
		int x = Integer.parseInt(nums[3]);
		
		int[] a = new int[n];
		
		line = br.readLine();
		nums = line.split(" ");
		for (int i=0; i<n; i++)
			a[i] = Integer.parseInt(nums[i]);
		
		int[] ratings = new int[n+1];
		ratings[0] = x;
		for (int i=0; i<n; i++)
			ratings[i+1] = ratings[i] + a[i];
		
		
//		for (int i=0; i<=n; i++)
//			System.out.print(ratings[i] + " ");
//		System.out.println();
		
		int[] inferiors = new int[n+1];
		if (ratings[0] < k)
			inferiors[0] = 1;
		
		for (int i=1; i<=n; i++) {
			if (ratings[i] < k) {
				inferiors[i] = inferiors[i-1] + 1;
			} else {
				inferiors[i] = inferiors[i-1];
			}				
		}
		
//		for (int i=0; i<=n; i++)
//			System.out.print(inferiors[i] + " ");
//		System.out.println();
		int l, r;
		for (int i=0; i<m; i++) {
			line = br.readLine();
			nums = line.split(" ");
			l = Integer.parseInt(nums[0]);
			r = Integer.parseInt(nums[1]);
			l--;
			r--;
			bw.write(inferiors[r] - inferiors[l] + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
		
	}
}
