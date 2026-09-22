// Código por Giovanni Sartori

#include <stdio.h>
#include <iostream>
using namespace std;

class Ex1Primos {
    private:
        int n;
        int resultado;

        // Complexidade O(n).
        int testarPrimo(int n){

            int i = 2, primo = 1;
            if(n < 2) return 0;

            // O maior valor que um divisor de n pode assumir é a raiz quadrada de n
            while(i * i <= n){
                if(!(n % i)){
                    primo = 0;
                    break;
                }
                i++;    
            }

            return primo;
        };
    public:
        Ex1Primos(int N){
            n = N;
            resultado = testarPrimo(n);
        };

        ~Ex1Primos(){};

        void getResultado(){
            resultado ? cout << "É primo!" << endl : cout << "Não é primo." << endl;
        };
};

int main(){
    Ex1Primos ex1(45);
    ex1.getResultado();

    return 0;
}