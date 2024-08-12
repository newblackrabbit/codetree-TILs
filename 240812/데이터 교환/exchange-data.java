public class Main {
    public static void main(String[] args) {
        int a = 5, b = 6, c = 7;
        int m;
        int n;
        m = a;
        n = b;
        a = c;
        c = n;
        b = m;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}