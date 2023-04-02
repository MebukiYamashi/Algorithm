package Baekjoon_daily.Tutorial;
import java.util.*;
import java.io.*;

public class B_2908 {
    public static void main(String[] args) throws IOException {
        BufferedReader bu = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer S = new StringTokenizer(bu.readLine(), " ");
        int a = Integer.parseInt(new StringBuilder(S.nextToken()).reverse().toString());
		int b = Integer.parseInt(new StringBuilder(S.nextToken()).reverse().toString());
        System.out.println(a > b ? a : b);
    }
}
