// Código por Pedro Neves

import java.util.Scanner;

public class Ex2Sorteio {
    Scanner sc;
    int random = -1;

    public Ex2Sorteio() {
        this.sc = new Scanner(System.in);
        this.random = (int) (Math.random() * 1001);
    }

    public void sorteio() {
        System.out.print("Digite seu palpite: ");
        int palpite = this.sc.nextInt();

        while(palpite != this.random){
            if(palpite  > this.random) {
                System.out.println("Seu palpite é maior que o número sorteado!");
            } else {
                System.out.println("Seu palpite é menor que o número sorteado!");
            }

            System.out.print("Tente novamente: ");
            palpite = this.sc.nextInt();
        }
        System.out.println("Voce acertou!");
    }

    public static void main(String[] args) {
        Ex2Sorteio obj = new Ex2Sorteio();
        obj.sorteio();
    }
}