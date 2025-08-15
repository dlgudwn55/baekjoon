import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int ans = 0;
    
    int n = sc.nextInt();
    String[] strings = new String[n];
    
    for (int i=0; i<n; i++)
      strings[i] = sc.next();
    
    // 가장 짧은 문자열 구하기
    String ref = strings[0];
    for (int i=1; i<n; i++) {
      if (strings[i].length() < ref.length())
        ref = strings[i];
    }
    
    int i = 0;
    int j = 0;
    while (i < ref.length() && j < ref.length()) {
      boolean flag = true;
      for (String s: strings) {
        if (!s.contains(ref.substring(i, j+1))) {
          flag = false;
          break;
        }
      }
      if (flag) {
        ans = Math.max(ans, j-i+1);
        j++;
      } else {
        i++;
        if (i>j)
          j++;
      }
    }
    System.out.println(ans);
  }
}