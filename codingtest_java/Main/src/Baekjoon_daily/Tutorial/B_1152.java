package Baekjoon_daily.Tutorial;
import java.util.*;
import java.io.*;

public class B_1152 {
    public static void main(String[] args) throws Exception {
        BufferedReader bu = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer S = new StringTokenizer(bu.readLine());
        System.out.print(S.countTokens());
        bu.close();
    }
}
