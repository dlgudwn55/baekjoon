import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Lecture {
    int weekday;
    int start;
    int end;

    public Lecture(int weekday, int start, int end) {
	this.weekday = weekday;
	this.start = start;
	this.end = end;
    }
}

public class Main {
    static int ans = 0;

    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	String line = br.readLine().trim();
	String[] tokens = line.split("\\s+");
	int n = Integer.parseInt(tokens[0]); // 수업의 개수
	int k = Integer.parseInt(tokens[1]); // 정확히 k 학점을 들어야 함

	List<Lecture> lectures = new ArrayList<>();

	for (int i = 0; i < n; i++) {
	    line = br.readLine().trim();
	    tokens = line.split("\\s+");
	    int w = Integer.parseInt(tokens[0]);
	    int s = Integer.parseInt(tokens[1]);
	    int e = Integer.parseInt(tokens[2]);

	    if (w != 5) {
		Lecture lecture = new Lecture(w, s, e);
		lectures.add(lecture);
	    }
	}

	boolean[] visited = new boolean[lectures.size()];
	generateSubsets(lectures, visited, 0, 0, k);
	System.out.println(ans);
    }

    public static void generateSubsets(List<Lecture> lectures, boolean[] visited, int depth, int totalCredit, int k) {
	if (depth == lectures.size()) {
//	    for (int i = 0; i < visited.length; i++) {
//		System.out.print(visited[i] + " ");
//	    }
//	    System.out.println();
	    if (totalCredit == k) {
		ans++;
	    }
	    return;
	}

	Lecture curLecture = lectures.get(depth);
	boolean isCandidate = true;
	for (int i = 0; i < depth; i++) {
	    if (visited[i]) {
		Lecture lecture = lectures.get(i);
		if (lecture.weekday == curLecture.weekday && !(lecture.end < curLecture.start || curLecture.end < lecture.start)) {
		    isCandidate = false;
		    break;
		}
	    }
	}

	// 강의에 넣을 수 있을 때만 포함
	if (isCandidate) {
	    visited[depth] = true;
	    int credit = curLecture.end - curLecture.start + 1;
	    generateSubsets(lectures, visited, depth + 1, totalCredit + credit, k);
	}

	visited[depth] = false;
	generateSubsets(lectures, visited, depth + 1, totalCredit, k);
    }
}