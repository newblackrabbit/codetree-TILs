import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = a + 1.5;
        System.out.println(Math.round(b*100)/100.0);
    }
}