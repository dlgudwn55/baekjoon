import java.util.HashMap;
import java.util.Scanner;

class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int u = sc.nextInt();
    int n = sc.nextInt();

    String[] names = new String[n];
    int[] prices = new int[n];

    for (int i = 0; i < n; i++) {
      names[i] = sc.next();
      prices[i] = sc.nextInt();
    }

    HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
    for (int i = 0; i < n; i++)
      h.put(prices[i], 0);

    for (int i = 0; i < n; i++)
      h.replace(prices[i], h.get(prices[i]) + 1);


    int targetPrice = 99999;
    int minCount = 999999;
    for (int price : h.keySet()) {
      int count = h.get(price);
      if (minCount > count) {
        targetPrice = price;
        minCount = count;
      } else if(minCount == count && targetPrice > price) {
        targetPrice = price;
      }
    }
    
    String winner = "No";
    for (int i=0; i<n; i++) {
      if (prices[i] == targetPrice) {
        winner = names[i];
        break;
      }
    }
    System.out.println(winner + " " + targetPrice);
  }

}
