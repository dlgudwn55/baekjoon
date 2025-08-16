import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i=0; i<n; i++) {
      String input = sc.next();
      int ans = input.indexOf("D");
      if (ans == -1)
        System.out.println(input.length());
      else
        System.out.println(input.indexOf("D"));
    }
  }

}
