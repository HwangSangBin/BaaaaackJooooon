import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int h, m, c, cnt;

        h = scanner.nextInt();
        m = scanner.nextInt();
        c = scanner.nextInt();

        if (m + c >= 60) {
            cnt = (m+c) / 60;
            h = h + cnt;
            m = (m+c) % 60;
        }
        else{
            m = m+c;
        }
        if (h >= 24){
            h = h - 24;
        }

        System.out.print(h);
        System.out.println(" " + m);
    }
}