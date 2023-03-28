package Baekjoon_daily.Tutorial;

import java.util.*;
import java.io.*;

public class B_1008 {
    public static void main(String[] args) throws Exception {
        BufferedReader bu = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer S = new StringTokenizer(bu.readLine());
        double a = Integer.parseInt(S.nextToken());
        double b = Integer.parseInt(S.nextToken());
        System.out.println(a/b);
        bu.close();
    }
}
