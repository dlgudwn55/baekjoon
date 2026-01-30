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

	char[][] transposedBoard = transposeBoard(board);
	
//	for (int i = 0; i < m; i++) {
//	    transposedBoard[i]
//	}
	for (int i = 0; i < m; i++) {
//	    if (!(transposedBoard[i].toString().contains("#"))) {
//		transposedBoard[i][0] = transposedBoard[i][0] == '#' ? ''
//	    }
//	    System.out.println("Line " + i);
	    int left = n - 1;
	    int right = n - 1;
	    int appleCount = 0;
//	    boolean isIn = false;
	    while (left >= 0 && right >= 0) {
//		br.readLine();
		if (transposedBoard[i][left] == '#') {
//		    System.out.println(left + " " + right + " " + appleCount);
		    for (int j = right; j > left; j--) {
			if (appleCount > 0) {
			    transposedBoard[i][j] = 'o';
			    appleCount--;
			} else {
			    transposedBoard[i][j] = '.';
			}
		    }
		    appleCount = 0;
		    left--;
		    right = left;
		} else {
		    if (transposedBoard[i][left] == 'o') {
			appleCount++;
		    }
		    left--;
		}
	    }
//	    System.out.println(left + " " + right + " " + appleCount);
	    for (int j = right; j > left; j--) {
		if (appleCount > 0) {
		    transposedBoard[i][j] = 'o';
		    appleCount--;
		} else {
		    transposedBoard[i][j] = '.';
		}
	    }
	}
	
	for (int i = 0; i < n; i++) {
	    for (int j = 0; j < m; j++) {
		System.out.print(transposedBoard[j][i]);
	    }
	    System.out.println();
	}
    }

    // n x m 배열 -> m x n 배열
    public static char[][] transposeBoard(char[][] board) {
	int n = board.length;
	int m = board[0].length;
	char[][] transposedBoard = new char[m][n];
	for (int i = 0; i < n; i++) {
	    for (int j = 0; j < m; j++) {
		transposedBoard[j][i] = board[i][j];
	    }
	}
	return transposedBoard;
    }
}