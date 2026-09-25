import java.util.Scanner;

public class Ex1Primos {

    public static boolean testarPrimo(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i * i <= n; i += 2) { //Testa todos os números impares até a raiz quadrada de n
            if (n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um número inteiro N: ");
        int n = sc.nextInt();

        if (testarPrimo(n)) {
            System.out.println(n + " é primo.");
        } else {
            System.out.println(n + " não é primo.");
        }

        sc.close();
    }
}