import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	String line = br.readLine();
	String[] tokens = line.trim().split("\\s+");
	int n = Integer.parseInt(tokens[0]);
	int m = Integer.parseInt(tokens[1]);

	char[][] board = new char[n][m];
	for (int i = 0; i < n; i++) {
	    line = br.readLine().trim();
	    for (int j = 0; j < m; j++) {
		    board[i][j] = line.charAt(j);
	    }
	}	

	for (int i = 0; i < m; i++) {
	    int up = n - 1;
	    int down = n - 1;
	    int appleCount = 0;
	    while (up >= 0 && down >= 0) {
		if (board[up][i] == '#') {
		    for (int j = down; j > up; j--) {
			if (appleCount > 0) {
			    board[j][i] = 'o';
			    appleCount--;
			} else {
			    board[j][i] = '.';
			}
		    }
		    appleCount = 0;
		    up--;
		    down = up;
		} else {
		    if (board[up][i] == 'o') {
			appleCount++;
		    }
		    up--;
		}
	    }
	    for (int j = down; j > up; j--) {
		if (appleCount > 0) {
		    board[j][i] = 'o';
		    appleCount--;
		} else {
		    board[j][i] = '.';
		}
	    }
	}
	
	for (int i = 0; i < n; i++) {
	    for (int j = 0; j < m; j++) {
		System.out.print(board[i][j]);
	    }
	    System.out.println();
	}
    }
}