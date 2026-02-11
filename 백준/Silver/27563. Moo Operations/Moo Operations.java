import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int q = Integer.parseInt(br.readLine());

        for (int i = 0; i < q; i++) {
            String s = br.readLine().trim();
            System.out.println(solve(s));
        }
    }

    public static int solve(String s) {
        if (s.length() < 3) {
            return -1;
        }

        int moo = s.indexOf("MOO");
        if (moo != -1) {
            return moo + s.length() - (moo + 3);
        }

        int mom = s.indexOf("MOM");
        if (mom != -1) {
            return mom + s.length() - (mom + 3) + 1;
        }

        int ooo = s.indexOf("OOO");
        if (ooo != -1) {
            return ooo + s.length() - (ooo + 3) + 1;
        }

        int oom = s.indexOf("OOM");
        if (oom != -1) {
            return oom + s.length() - (oom + 3) + 2;
        }

        return -1;
    }
}
