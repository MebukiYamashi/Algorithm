package Baekjoon_daily.Tutorial;
import java.io.*;

public class B_9408 {
    public static void main(String[] args) throws IOException {
        BufferedReader re = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(re.readLine());
        int comp = n / 10;
        String Grade = comp == 10 || comp == 9 ? "A": comp == 8 ? "B": comp == 7 ? "C": comp == 6 ? "D" : "F";
        System.out.println(Grade);
    }
}
