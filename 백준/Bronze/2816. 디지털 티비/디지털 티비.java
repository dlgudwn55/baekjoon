import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int n = sc.nextInt();
    String[] channels = new String[n];
    for (int i=0; i<n; i++) {
      channels[i] = sc.next();
    }
    
    String ans = "";
    int idx1 = 0;
    while (!channels[idx1].equals("KBS1")) {
      ans += "1";
      idx1 += 1;
    }
    ans += "4".repeat(idx1);
         
    int idx2 = 0;
    while (!channels[idx2].equals("KBS2")) {
      ans += "1";
      idx2 += 1;
    }
    if (idx1 > idx2) {
      ans += "14";
    }
    ans += "4".repeat(idx2-1);
       
    System.out.println(ans);
  }
}