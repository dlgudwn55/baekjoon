import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
//	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	Scanner scanner = new Scanner(System.in);
	
	int k = scanner.nextInt();
	int pp = 0;
	int p = 1;
	
	for (int i=0; i<k-1; i++) {
	    int tmp = p;
	    p = pp + p;
	    pp = tmp;
	}
	
	System.out.println(pp + " " + p);

	scanner.close();
    }
}