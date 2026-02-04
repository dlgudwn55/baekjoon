import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	List<Integer> primes = getPrimes();
	
	int n;
	while (true) {
	    n = Integer.parseInt(br.readLine().trim());
	    if (n == -1) {
		return;
	    }
	    
	    Set<Integer> factors = new LinkedHashSet<>();
	    int idx = 0;
	    int curN = n;
	    while (curN > 1) {
		if (curN % primes.get(idx) != 0) {
		    idx++;
		} else {
		    factors.add(primes.get(idx));
		    curN /= primes.get(idx);
		}
	    }
	    
	    boolean res = true;
	    for (Integer factor : factors) {
		if (!factor.toString().endsWith("3")) {
		    res = false;
		    break;
		}
	    }
	    if (res) {
		System.out.println(n + " YES");
	    } else {
		System.out.println(n + " NO");
	    }
	}

    }

    public static List<Integer> getPrimes() {
	// 에라토스테네스의 체 생성
	Map<Integer, Boolean> eratos = new LinkedHashMap();
	for (int i = 2; i < 1_000_001; i++) {
	    eratos.put(i, true);
	}

	for (int i = 2; i < 1_000_001; i++) {
	    if (eratos.get(i)) {
		for (int j = i * 2; j < 1_000_001; j += i) {
		    eratos.replace(i, false);
		}
	    }
	}

	// 소수 리스트 생성
	List<Integer> primes = new ArrayList<>();
	for (Map.Entry<Integer, Boolean> entry : eratos.entrySet()) {
	    Integer key = entry.getKey();
	    primes.add(key);
	}

	return primes;
    }
}