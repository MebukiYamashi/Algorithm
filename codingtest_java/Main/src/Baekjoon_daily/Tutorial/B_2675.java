package Baekjoon_daily.Tutorial;
import java.io.*;
import java.util.*;

public class B_2675 {
    public static void main(String[] args) throws Exception {
        BufferedReader bu = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder S = new StringBuilder();
        StringTokenizer st = new StringTokenizer(bu.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int i = 0; i < T; i++) {
            String[] str = bu.readLine().split(" ");
            int R = Integer.parseInt(str[0]);
            for (byte val : str[1].getBytes()) {
                for (int j = 0; j < R; j++) { 
                    S.append((char)val);
                }
            }
            S.append('\n');
        }
        System.out.println(S);
        bu.close();
    }
}
