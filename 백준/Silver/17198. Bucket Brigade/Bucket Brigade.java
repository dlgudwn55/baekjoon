import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

class Point {
    int x, y;
}

public class Main {
    public static void main(String[] args) {
	final int[] dx = {-1, 1, 0, 0};
	final int[] dy = {0, 0, -1, 1};
	
	Scanner scanner = new Scanner(System.in);
	
	String[] farm = new String[10];
	for (int i = 0; i < 10; i++) {
	    String row = scanner.nextLine();
	    farm[i] = row;
	}
	
	int[][] visit = new int[10][10];
	Point lake = new Point();
	
	for (int i = 0; i < 10; i++) {
	    for (int j = 0; j < 10; j++) {
		if (farm[i].charAt(j) == 'L') {
		    visit[i][j] = 0;
		    lake.x = i;
		    lake.y = j;
		} else {
		    visit[i][j] = -1;
		}
	    }
	}
	

	
	Deque<Point> deque = new ArrayDeque<>();
	deque.addLast(lake);
	while (deque.size() > 0) {
	    Point curr = deque.pollFirst();
	    if (farm[curr.x].charAt(curr.y) == 'B') {
		System.out.println(visit[curr.x][curr.y]-1);
		return;
	    }
	    for (int i = 0; i < 4; i++) {
		int nx = curr.x + dx[i];
		int ny = curr.y + dy[i];
		if (nx >= 0 && nx < 10 && ny >= 0 && ny < 10 &&  // 좌표 범위내
			visit[nx][ny] == -1 &&  // 미방문
			farm[nx].charAt(ny) != 'R'  // 바위가 아님
			) {
		    visit[nx][ny] = visit[curr.x][curr.y] + 1;
		    Point adj = new Point();
		    adj.x = nx;
		    adj.y = ny;
		    deque.addLast(adj);
		}
	    }
	}
	
//	for (int i = 0; i < 10; i++) {
//	    for (int j = 0; j < 10; j++) {
//		System.out.printf("  %d", visit[i][j]);
//	    }
//	    System.out.println();
//	}
    }
}