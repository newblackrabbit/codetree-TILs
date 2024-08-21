import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        String aa = String.format("%.3f",a);
        String bb = String.format("%.3f",b);
        String cc = String.format("%.3f",c);
        System.out.println(aa);
        System.out.println(bb);
        System.out.println(cc);
    }
}