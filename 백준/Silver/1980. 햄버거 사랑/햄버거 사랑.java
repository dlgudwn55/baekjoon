import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int n = sc.nextInt();
    int m = sc.nextInt();
    int t = sc.nextInt();
    
    int hamburger = 0;
    int cola = 9999;
    
    for (int i=0; i<=t/n; i++) {
      for (int j=0; j<=t/m; j++) {
        if (t - n*i - m*j >= 0 && t - n*i - m*j < cola) {
          cola = t - n*i - m*j;
          hamburger = i+j;
        } else if (t - n*i - m*j >= 0 && t - n*i - m*j == cola && i+j > hamburger) {
          hamburger = i+j;
        }
      }
    }
    
    System.out.println(hamburger + " " + cola);
  }
}