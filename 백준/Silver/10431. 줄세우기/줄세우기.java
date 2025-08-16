import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int p = sc.nextInt();
    
    for (int tn=1; tn<=p; tn++) {
      int ans = 0;
      int t = sc.nextInt();
      int[] heights = new int[20];
      
      for (int i=0; i<20; i++) {
        heights[i] = sc.nextInt();
      }
      
      int[] line = new int[20];
      line[0] = heights[0];
      
      for (int i=1; i<20; i++) {
        int height = heights[i];
        int j = 0;
        while (j < i && line[j] < height) {
          j++;
        }
        
        if (j == i) {
          line[j] = heights[i];
        } else {
          for (int k=i; k>j; k--) {
            line[k] = line[k-1];
            ans++;
          }
          line[j] = heights[i];
        }
        
      }
      System.out.println(t + " " + ans);
    }
    
  }
}