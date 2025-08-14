import java.util.Scanner;

class Main {
  public static int[] changeBase(int num, int base, int digit) {
    int[] res = new int[digit];
    int idx = 0;
    while (num > 0) {
      res[idx] = num % base;
      num /= base;
      idx++;
    }
    return res;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    
    for (int tn=1; tn<=t; tn++) {
      long ans = 0;
      
      int m = sc.nextInt();
      int n = sc.nextInt();
      
      int max = (int)Math.pow(m, n) - 1;

      for (int i=0; i<=max; i++) {
    	  int[] tmp = changeBase(i, m, n);
//    	  for (int digit: tmp)
//    	    System.out.print(digit);
//    	  System.out.println();
    	  boolean[] visit = new boolean[m];
    	  for (int digit: tmp) {
    	    visit[digit] = true;
    	  }
    	  
    	  boolean flag = true;
    	  for (int j=0; j<m; j++) {
          if (!visit[j]) {
            flag = false;
            break;
          }
        }
    	  if (flag) {
    	    ans++;
    	  }
      }
      
      
      System.out.println("Case #" + tn + ": " + ans % 1000000007);
    }
  }

}
